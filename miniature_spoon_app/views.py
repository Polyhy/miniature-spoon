from flask import render_template, redirect
from sqlalchemy.orm import scoped_session

from miniature_spoon_app import app, SessionFactory
from link.model import Link


@app.route('/', methods=['GET'])
def show():
    return render_template('pages/index.html')

@app.route('/<token>', methods=['GET'])
def redirectShortURL(token):
    session = scoped_session(SessionFactory)
    s = session.query(Link).filter(Link.shortLink == token)
    if s.count() > 0:
        link = s[0]
        url = link.originalLink
        link.click = link.click + 1
        session.commit()
        session.remove()
        return redirect("http://www."+url, 302)
    else:
        return render_template('404.html')
