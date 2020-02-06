from flask import Flask
from app.database import db
from app.redis import redis_client
import logging
import graypy
import os
from app.config import config

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    app.after_request(after_request)
    # app.config['REDIS_URL'] = 'redis://localhost:6379/0'
    db.init_app(app)
    db.app = app
    redis_client.init_app(app)
    return app


# Support Cross Domain
def after_request(resp):
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Access-Control-Allow-Headers'] = '*'
    return resp


def init_logger():
    # init logger for Graylog
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    handler = graypy.GELFUDPHandler(config.GRAYLOG_HOST, 12201)
    logger.addHandler(handler)
    return logger