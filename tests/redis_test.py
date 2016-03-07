import unittest
import redis
from miniature_spoon_app.config import  REDIS_HOST, REDIS_PORT, REDIS_DB


class RedisTest(unittest.TestCase):
    def test_redis_connection(self):
        redis_conn = redis.StrictRedis(REDIS_HOST, REDIS_PORT, REDIS_DB)
        self.assertEqual(redis_conn.get("test"), None)
        redis_conn.set("test", 1)
        self.assertEqual(redis_conn.get("test"), '1')
        redis_conn.delete("test")
        self.assertEqual(redis_conn.get("test"), None)
