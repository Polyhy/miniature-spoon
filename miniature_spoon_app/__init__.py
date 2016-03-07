from flask import Flask
from flask_cache import Cache
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import config

app = Flask(__name__)
cache = Cache(app, config={
    'CACHE_TYPE': 'redis',
    'CACHE_KEY_PREFIX': config.REDIS_PREFIX,
    'CACHE_REDIS_HOST': config.REDIS_HOST,
    'CACHE_REDIS_PORT': config.REDIS_PORT,
    'CACHE_REDIS_URL': config.REDIS_URL
})

engine = create_engine(config.SQLALCHEMY_DATABASE_URI, echo=True)

SessionFactory = sessionmaker(autocommit=False, autoflush=True, bind=engine,
                              expire_on_commit=False)
Base = declarative_base()

from miniature_spoon_app.link.views import links as linkModule
import miniature_spoon_app.views

app.register_blueprint(linkModule)

Base.metadata.create_all(bind=engine)
