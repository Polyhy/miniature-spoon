DEBUG = True

import os
_basedir = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = "hellominiaturespoon"

# SQLALCHEMY
SQLALCHEMY_DATABASE_URI = 'mysql://root:password@localhost/miniature_spoon'
DATABASE_CONNECT_OPTIONS = {}
