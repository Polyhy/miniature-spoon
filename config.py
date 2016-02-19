DEBUG = True

import os

_basedir = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = "hellominiaturespoon"

# SQLALCHEMY
# SQLALCHEMY_DATABASE_URI = 'mysql://root:tkdaud1004@localhost/miniature_spoon'
DATABASE_USER_ID = 'root'
DATABASE_USER_PASSWD = 'tkdaud1004'
DATABASE_NAME = 'miniature_spoon'
DATABASE_PORT = 3306
DATABASE_ADDR = 'localhost'
SQLALCHEMY_DATABASE_URI = 'mysql://%s:%s@%s/%s' % (
    DATABASE_USER_ID, DATABASE_USER_PASSWD, DATABASE_ADDR, DATABASE_NAME)
