import logging
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = None


def get_url():
    host = os.getenv('POSTGRES_HOST')
    port = os.getenv('POSTGRES_PORT')
    username = os.getenv('POSTGRES_USER')
    password = os.getenv('POSTGRES_PASS')
    db = os.getenv('POSTGRES_DB')

    if os.getenv('ENV') != 'local':
        conn_url = f'postgresql+pg8000://{username}:{password}@/{db}?unix_sock={host}'
    else:
        conn_url = f'postgresql+psycopg2://{username}:{password}@{host}:{port}/{db}'

    return conn_url


def get_engine():
    global engine
    if not engine:
        pool_size = os.getenv("POOL_SIZE")
        max_overflow = os.getenv("MAX_OVERFLOW")
        engine = create_engine(
            get_url(),
            pool_size=int(pool_size),
            max_overflow=int(max_overflow)
        )
        engine.connect()
        logging.info(
            'Database connection established'
        )
    return engine


def new_session():
    _engine = get_engine()
    session = scoped_session(sessionmaker())
    session.configure(bind=_engine, autoflush=False, expire_on_commit=False)
    return session

# for local only!!!
# def init_database():
#     engine = get_engine()
#     Base.metadata.drop_all(engine)
#     Base.metadata.create_all(engine)
