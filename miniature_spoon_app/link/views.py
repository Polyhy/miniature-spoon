from flask import Blueprint, request, flash, g, session, redirect, url_for


links = Blueprint('links', __name__, url_prefix='/v1/link')
@links.route('/', methods=['GET'])
def test():
    return "work"
