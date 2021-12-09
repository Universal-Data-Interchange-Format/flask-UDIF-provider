import os

from gevent.pool import Pool
from gevent.pywsgi import WSGIServer

from app.api import app

if __name__ == '__main__':
    pool = Pool(int(os.getenv("GEVENT_POOL_SIZE", "50")))

    server = WSGIServer(('0.0.0.0', 5000), app, spawn=pool)

    if server is not None:
        server.serve_forever()