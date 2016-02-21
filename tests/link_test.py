import os
import miniature_spoon_app as miniatureSpoon
import unittest
import tempfile
import jwt


class LinkTest(unittest.TestCase):
    def setUp(self):
        self.db_fd, miniatureSpoon.app.config['DATABASE'] = tempfile.mkstemp()
        miniatureSpoon.app.config['TESTING'] = True
        self.app = miniatureSpoon.app.test_client()
        miniatureSpoon.declarative_base()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(miniatureSpoon.app.config['DATABASE'])

    def test_get(self):
        # rv = self.app.get('/v1/link')
        # assert 'No entries here so far' in rv.data
        print("test")

    def test_post(self):
        # data = jwt.encode({'link': 'naver.com'}, 'hellominiaturespoon', algorithm='HS256')
        # rv = self.app.post(('/v1/link', data))
        # print(rv.data)
        # assert 'No entries here so far' in rv.data
        print("test")


if __name__ == '__main__':
    unittest.main()
