from flask import Blueprint, render_template, request, flash, g, session, redirect, url_for, abort
from jinja2 import TemplateNotFound

pages = Blueprint('pages', __name__, template_folder='templates')

@pages.route('/', methods = ['GET'], defaults={'page': 'index'})

@pages.route('/<page>',  methods = ['GET'])
def show(page):
    try:
        return render_template('pages/%s.html' % page)
    except TemplateNotFound:
        return render_template('404.html')