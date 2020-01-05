from flask import Flask
from app.database import db

import os


def create_app(config=None):
    app = Flask(__name__)
    app.config.from_pyfile('database/config.py')
    if isinstance(config, dict):
        app.config.update(config)
    elif config:
        app.config.from_pyfile(os.path.realpath(config))
    app.after_request(after_request)

    db.init_app(app)
    db.app = app

    return app


# 跨域支持
def after_request(resp):
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp
