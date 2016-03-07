import json
import tempfile
import unittest

import jwt
import os

import miniature_spoon_app as miniatureSpoon
from miniature_spoon_app import redis_conn


class LinkTest(unittest.TestCase):
    def setUp(self):
        self.db_fd, miniatureSpoon.config.DATABASE = tempfile.mkstemp()
        miniatureSpoon.config.TESTING = True
        self.app = miniatureSpoon.app.test_client()
        miniatureSpoon.declarative_base()

    def tearDown(self):
        os.close(self.db_fd)
        # os.unlink(miniatureSpoon.config.DATABASE)

    def test_shortURL(self):
        url = 'http://www.facebook.com'
        requestData = jwt.encode({'link': url}, 'hellominiaturespoon',
                                 algorithm='HS256')
        rv = self.app.post('/v1/link', data=requestData)
        data = json.loads(rv.data)
        self.assertEqual(rv._status_code, 201, "POST request is failed")

        rv2 = self.app.get('/v1/link?request_id=' + str(data['request_id']))
        data2 = json.loads(rv2.data)
        self.assertEqual(rv2._status_code, 200, "GET request is failed")
        self.assertEqual(data['short_url'], data2['short_url'],
                         "Get short url by request id is failed")

        rv3 = self.app.get(str(data['short_url']), follow_redirects=False)
        self.assertEqual(rv3._status_code, 302,
                         "Can not redirect to original link with short link")
        self.assertEqual(rv3.location, url,
                         "Can not redirect to original link with short link")

        requestData2 = jwt.encode({'request_id': data['request_id']},
                                  'hellominiaturespoon', algorithm='HS256')
        rv4 = self.app.delete('/v1/link', data=requestData2)
        self.assertEqual(rv4._status_code, 200,
                         "Failed to delete url from db")


class RedisTest(unittest.TestCase):
    def test_redis_connection(self):
        redis_conn.set("test", 1)
        print redis_conn.get("test")


if __name__ == '__main__':
    unittest.main()
