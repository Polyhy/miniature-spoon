from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

app = Flask(__name__)
app.config.from_object('config')

engine = create_engine(app.config["SQLALCHEMY_DATABASE_URI"], echo=True)

SessionFactory = sessionmaker(autocommit=False, autoflush=True, bind=engine,
                              expire_on_commit=False)
Base = declarative_base()

from miniature_spoon_app.link.views import links as linkModule
import miniature_spoon_app.views

app.register_blueprint(linkModule)

Base.metadata.create_all(bind=engine)
