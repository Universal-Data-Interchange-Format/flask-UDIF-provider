import os

from gevent.pool import Pool
from gevent.pywsgi import WSGIServer

from app.api import app

if __name__ == '__main__':
    pool = Pool(int(os.getenv("GEVENT_POOL_SIZE", "50")))

    # Server environment
    server = None

    if os.environ.get('ENV') != 'production':
        server = WSGIServer(('0.0.0.0', 5000), app, spawn=pool)
    else:
        server = WSGIServer(('0.0.0.0', os.environ.get('PORT')), app, spawn=pool)

    if server is not None:
        server.serve_forever()
