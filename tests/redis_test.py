import unittest

from miniature_spoon_app import redis_conn


class RedisTest(unittest.TestCase):
    def test_redis_connection(self):
        self.assertEqual(redis_conn.get("test"), None)
        redis_conn.set("test", 1)
        self.assertEqual(redis_conn.get("test"), '1')
        redis_conn.delete("test")
        self.assertEqual(redis_conn.get("test"), None)
