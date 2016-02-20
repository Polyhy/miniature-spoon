from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

app = Flask(__name__)
app.config.from_object('config')

# db = SQLAlchemy(app)
engine = create_engine(app.config["SQLALCHEMY_DATABASE_URI"], echo=True)

SessionFactory = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = scoped_session(SessionFactory)

Base = declarative_base()

from miniature_spoon_app.link.views import links as linkModule
from miniature_spoon_app.views import pages

app.register_blueprint(pages)
app.register_blueprint(linkModule)

Base.metadata.create_all(bind=engine)
