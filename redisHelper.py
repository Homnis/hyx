import redis


class redisHelper():
    def __init__(self, host="localhost", port=6379):
        self.redis = redis.StrictRedis(host, port)

    def getRedis(self, key):
        if self.redis.exists(key):
            return self.redis.get(key)
        else:
            return ""

    def set(self, key, value):
        self.redis.set(key, value)
