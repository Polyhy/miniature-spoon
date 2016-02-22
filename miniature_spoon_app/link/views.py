from flask import Blueprint, request, make_response, jsonify
import jwt
from sqlalchemy.orm import scoped_session

from model import Link
from link_shortner import makeMiniature
from utils.convertDictToStr import convertDictToStr
from miniature_spoon_app import SessionFactory

from miniature_spoon_app import app

links = Blueprint('links', __name__, url_prefix='/v1/link')


@links.route('', methods=['POST'])
def postShortURL():
    if not request.data:
        return make_response(jsonify({'status': 'body data is none'}), 400)
    bodyData = convertDictToStr(
        jwt.decode(request.data, app.config['SECRET_KEY'], algorithm=['HS256']))
    if not 'link' in bodyData:
        return make_response(jsonify({'status': 'link is none'}), 400)
    originalLink = bodyData.get('link')
    session = scoped_session(SessionFactory)
    link = Link(originalLink)
    session.add(link)
    session.flush()
    link.shortLink = makeMiniature(int(link.id))
    session.commit()
    session.remove()
    responseData = {
        'request_id': link.id,
        'short_url': request.url_root.encode() + link.shortLink
    }
    response = make_response(jsonify(responseData), 201)
    return response


@links.route('', methods=['GET'])
def getShortURL():
    if not 'request_id' in request.args:
        return make_response(jsonify({'status': 'request_id is none'}), 400)
    requestId = request.args.get('request_id')
    print requestId
    session = scoped_session(SessionFactory)
    s = session.query(Link).filter(Link.id == requestId)
    session.remove()
    if s.count() > 0:
        link = s[0]
        responseData = {'short_url': request.url_root.encode() + link.shortLink}
        response = make_response(jsonify(responseData), 200)
        return response
    else:
        return make_response(jsonify({'status': 'can not find'}), 404)


@links.route('', methods=['DELETE'])
def deleteShortURL():
    if not request.data:
        return make_response(jsonify({'status': 'body data is none'}), 400)
    bodyData = convertDictToStr(
        jwt.decode(request.data, app.config['SECRET_KEY'], algorithm=['HS256']))
    if not 'request_id' in bodyData:
        return make_response(jsonify({'status': 'request_id is none'}), 400)
    requestId = bodyData.get('request_id')
    session = scoped_session(SessionFactory)
    s = session.query(Link).filter(Link.id == requestId)
    if s.count() == 1:
        session.delete(s[0])
        session.commit()
        session.remove()
        responseData = {'status': 'request %d is deleted' % requestId}
        return make_response(jsonify(responseData), 200)
    else:
        return make_response(jsonify({'status': 'can not find'}), 404)
