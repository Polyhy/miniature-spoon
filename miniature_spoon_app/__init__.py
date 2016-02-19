from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)

from miniature_spoon_app.views import pages
app.register_blueprint(pages)

from miniature_spoon_app.link.views import links as linkModule
app.register_blueprint(linkModule)

db.metadata.create_all()