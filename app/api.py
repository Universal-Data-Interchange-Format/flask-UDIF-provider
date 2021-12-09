import json
import os
import time
import uuid
from datetime import datetime

# Load .env
from dotenv import load_dotenv

load_dotenv()

# Load Flask
from flask import Flask, g, request
from flask_cors import CORS
import logging

# Set up logging level
from app.pg import new_session

# Load blueprints
from .blueprints import healthz, udif_creator

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(module)s %(name)s.%(funcName)s +%(lineno)s: %(levelname)-8s [%('
                           'process)d] %(message)s',
                    )
logging.info('Flask app created')

###########################
# Initialize the Flask App
###########################
app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False
app.config['JSON_SORT_KEYS'] = False
#####################################
# Setup CORS for the app
#####################################
streamlytics_urls = [r'https://.+clture\.io$']

if "PROD" in os.getenv('ENV').upper():
    streamlytics_urls = [r'https://.+clture\.io$']
else:
    streamlytics_urls = ['*']

CORS(
    app,
    supports_credentials=True,
    resources={
        r"/*": {
            "origins": streamlytics_urls,
            "allow_headers": [
                'origin',
                'x-requested-with',
                'accept',
                'Content-Type',
                'Authorization'
            ]
        },
        "/": {
            "origins": streamlytics_urls,
            "allow_headers": [
                'origin',
                'x-requested-with',
                'accept',
                'Content-Type',
                'Authorization'
            ]
        }
    }
)


#################################################
# Only for development comment out when deploying
#################################################
# if os.environ.get('APPLY_SCHEMA') == 'true':
#     app.logger.warning("Clearing DB to apply schema")
#     init_database()
#     init_database()


#####################################
# Request-lifetime hooks
#####################################
@app.before_request
def get_session():
    g.request_start_time = datetime.utcnow()
    g.request_id = str(uuid.uuid4())
    g.session = new_session()


@app.after_request
def close_session(response):
    g.response_status_code = response.status_code
    if hasattr(g, 'request_id'):
        response.headers['Request-Id'] = g.request_id
    return response


@app.teardown_request
def teardown_request(exception=None):
    url_params = request.url.split('?')
    if len(url_params) > 1:
        params = url_params[1]
    else:
        params = None
    if hasattr(g, 'response_status_code') and g.response_status_code:
        response_status_code = g.response_status_code
    else:
        response_status_code = 500
    if hasattr(g, 'request_start_time'):
        response_diff = datetime.utcnow() - g.request_start_time
        response_time = response_diff.total_seconds() * 1000
    else:
        response_time = 0
    if request.url_rule:
        rule = request.url_rule.rule
        endpoint = request.url_rule.endpoint
    else:
        rule = None
        endpoint = None
    if exception:
        log_level = logging.ERROR
    else:
        log_level = logging.INFO
    try:
        body = json.loads(request.data.decode("utf-8"))
    except ValueError:
        body = None
    app.logger.log(log_level, {
        'msg': 'Api Request',
        'url': request.base_url,
        'method': request.method,
        'params': params,
        'view_args': request.view_args,
        'body': body,
        'rule': rule,
        'endpoint': endpoint,
        'status_code': response_status_code,
        'milliseconds': response_time,
        'request_ip': request.headers.get('X-Forwarded-For')
    }, exc_info=exception)


app.logger.info("Request hooks set")

from celery import Celery


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
    CELERY_BROKER_URL='redis://localhost:6379',
    CELERY_RESULT_BACKEND='redis://localhost:6379'
)
celery = make_celery(app)


@celery.task()
def add_together():
    print(1231231231)
    time.sleep(100)
    pass


#####################################
# Endpoint Definitions and Blueprints
#####################################
app.register_blueprint(healthz, url_prefix='/')
app.register_blueprint(udif_creator, url_prefix='/create-udif')
