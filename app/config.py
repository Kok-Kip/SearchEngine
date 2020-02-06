import os


class BaseConfig:
    ACCESS_KEY = os.getenv('ACCESS_KEY')
    ACCESS_SECRET = os.getenv('ACCESS_SECRET')
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI',
                                        'mysql+pymysql://root:******@127.0.0.1:3306/search_engine?charset=utf8')
    SQLALCHEMY_COMMIT_ON_TEARDOWN = os.getenv('SQLALCHEMY_COMMIT_ON_TEARDOWN', True)
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS', True)
    SQLALCHEMY_POOL_SIZE = os.getenv('SQLALCHEMY_POOL_SIZE', 10)
    SQLALCHEMY_MAX_OVERFLOW = os.getenv('SQLALCHEMY_MAX_OVERFLOW', 5)
    REDIS_URL = os.getenv('REDIS_URL', 'redis://127.0.0.1:6379/0')
    GRAYLOG_HOST = os.getenv('GRAYLOG_HOST', 'localhost')

config = BaseConfig
