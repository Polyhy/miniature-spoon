from flask import Blueprint, request, flash, g, session, redirect, url_for
from miniature_spoon_app import db
from miniature_spoon_app.link.model import Link

links = Blueprint('links', __name__, url_prefix='/v1/link')


@links.route('/', methods=['GET'])
def test():
    return "work"
