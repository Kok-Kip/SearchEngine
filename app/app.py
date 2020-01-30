from flask import Flask
from app.database import db
from app.redis import redis_client
import os


def create_app(config=None):
    app = Flask(__name__)
    app.config.from_pyfile('database/config.py')
    if isinstance(config, dict):
        app.config.update(config)
    elif config:
        app.config.from_pyfile(os.path.realpath(config))
    app.after_request(after_request)
    app.config['REDIS_URL'] = 'redis://localhost:6379/0'
    db.init_app(app)
    db.app = app
    redis_client.init_app(app)
    return app


# Support Cross Domain
def after_request(resp):
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Access-Control-Allow-Headers'] = '*'
    return resp
