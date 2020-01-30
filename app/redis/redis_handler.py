from app.redis import redis_client


def get(key):
    return redis_client.get(key)

def set(key, value):
    redis_client.set(key, value)