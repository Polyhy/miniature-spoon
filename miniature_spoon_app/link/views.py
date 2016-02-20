from flask import Blueprint, request, flash, g, session, redirect, url_for
from miniature_spoon_app.link.model import Link

links = Blueprint('links', __name__, url_prefix='/v1/link')


@links.route('/', methods=['POST'])
def postShortURL():
    bodyData = request.data
    return "work"


@links.route('/', methods=['GET'])
def getShortURL():
    # session = db.scoped_session(
    #     db.sessionmaker(bind=db.engine, autocommit=False, autoflush=False))
    return "work"
