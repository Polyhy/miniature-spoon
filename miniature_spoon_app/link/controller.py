from flask import request
from sqlalchemy.orm import scoped_session

from miniature_spoon_app import SessionFactory
from miniature_spoon_app import cache, config
from miniature_spoon_app.link.link_shortner import makeMiniature
from model import Link


def getOriginalUrl(token):
    session = scoped_session(SessionFactory)
    shortURL = token.encode()
    s = session.query(Link).filter(Link.shortLink == shortURL)
    if s.count() > 0:
        link = s[0]
        # link.click = link.click + 1
        session.commit()
        session.remove()
        return 200, link
    else:
        return 404, None


def addNewLink(originalLink):
    session = scoped_session(SessionFactory)
    link = Link(originalLink)
    session.add(link)
    session.flush()
    link.shortLink = makeMiniature(int(link.id))
    session.commit()
    session.remove()
    result = {
        'request_id': link.id,
        'short_url': request.url_root.encode() + link.shortLink
    }
    return 201, result


def getShortLink(requestId):
    session = scoped_session(SessionFactory)
    s = session.query(Link).filter(Link.id == requestId)
    session.remove()
    if s.count() > 0:
        result = {'short_url': request.url_root.encode() + s[0].shortLink}
        return 200, result
    else:
        return 404, {'status': 'can not find'}


def deleteLink(requestId):
    session = scoped_session(SessionFactory)
    s = session.query(Link).filter(Link.id == requestId)
    if s.count() == 1:
        session.delete(s[0])
        session.commit()
        session.remove()
        result = {'status': 'request %d is deleted' % requestId}
        return 200, result
    else:
        session.remove()
        return 404, {'status': 'can not find'}
