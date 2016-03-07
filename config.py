DEBUG = True

import os

_basedir = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = "hellominiaturespoon"
HOST = "127.0.0.1"
PORT = "8080"

# SQL ALCHEMY
DATABASE_USER_ID = "root"
DATABASE_USER_PASSWD = "tkdaud1004"
DATABASE_NAME = "miniature_spoon"
DATABASE_PORT = 3306
DATABASE_ADDR = "localhost"
SQLALCHEMY_DATABASE_URI = "mysql://%s:%s@%s/%s" % (
    DATABASE_USER_ID, DATABASE_USER_PASSWD, DATABASE_ADDR, DATABASE_NAME)

# Redis
REDIS_PREFIX = os.getenv("REDIS_PREFIX", "short:")
REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", "6379"))
REDIS_DB = int(os.getenv("REDIS_DB", "0"))
