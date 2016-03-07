import unittest

from miniature_spoon_app import redis_conn


class RedisTest(unittest.TestCase):
    def test_redis_connection(self):
        redis_conn.set("test", 1)
        print redis_conn.get("test")
