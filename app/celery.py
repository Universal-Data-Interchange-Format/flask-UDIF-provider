import json
import os

import requests
from celery import Celery
# Load .env
from dotenv import load_dotenv
from flask import Flask
from sqlalchemy import create_engine

from app.pg import get_url
from app.utils import client, upload_data_with_zip

load_dotenv()

app = Flask(__name__)


def make_celery(app):
    celery = Celery(
        app.import_name,
        backend=app.config['CELERY_RESULT_BACKEND'],
        broker=app.config['CELERY_BROKER_URL']
    )
    celery.conf.update(app.config)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery


app.config.update(
    CELERY_BROKER_URL=f'redis://{os.getenv("REDIS_URL")}:6379/0',
    CELERY_RESULT_BACKEND=f'redis://{os.getenv("REDIS_URL")}:6379/0'
)
celery = make_celery(app)


#####################################
# Celery Tasks
#####################################
@celery.task()
def celery_health_check() -> bool:
    print('Celery Running properly.')
    return True


@celery.task()
def celery_process_udif(user_id: str, username: str, requested_datetime: str) -> None:
    print(f'{username}\'s Celery working')
    gql_url = os.getenv('GRAPHQL_URL')
    try:
        print("About to connect to DB.")

        session = create_engine(get_url(), connect_args={}).connect()
        query = """select id from users_upload where user_id = '%s'""" % user_id
        result = session.execute(query)
        session.close()

        print("Database connection has been closed")

        t_list = []
        for (upload_id,) in result:
            try:
                gql_query = """
                        query MyQuery {   
                          usersContentMapping(uploadId: %s) {
                            users {
                              service
                              gender
                              contents
                              serviceProvider
                              serviceProviderType
                              activityType
                              activity
                              dateOfBirth
                              userId
                              collection
                              uploadId
                            }
                          }
                        }
                        """ % upload_id
                result: dict = requests.post(url=gql_url, json={'query': gql_query}).json()
                t_list.extend(result["data"]['usersContentMapping']["users"])
            except KeyError:
                print("error_id", upload_id)

        message = 'User has not data'
        if t_list:
            text: str = json.dumps(t_list)
            processed_file_url: str = upload_data_with_zip(
                client=client,
                bucket_name=os.getenv('BUCKET_NAME'),
                blob_name=f"{username}_{requested_datetime}",
                file_name=f"{username}_{requested_datetime}.json",
                data=text
            )
            message = processed_file_url
            print(message)
        requests.post(url=os.getenv('WEBHOOK_URL'), json={'data': message})

        print(f'{username}\'s Celery Task has been completed.')

    except Exception as e:
        message = f'{e.__str__()}'
        requests.post(url=os.getenv('WEBHOOK_URL'), json={'error': message})
