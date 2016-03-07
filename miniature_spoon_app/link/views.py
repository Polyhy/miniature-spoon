import jwt
from flask import Blueprint, request, make_response, jsonify

from miniature_spoon_app import config
from miniature_spoon_app.link import controller as linkController
from utils.convertDictToStr import convertDictToStr

links = Blueprint('links', __name__, url_prefix='/v1/link')


@links.route('', methods=['POST'])
def postShortURL():
    if not request.data:
        return make_response(jsonify({'status': 'body data is none'}), 400)
    bodyData = convertDictToStr(
        jwt.decode(request.data, config.SECRET_KEY, algorithm=['HS256']))
    if not 'link' in bodyData:
        return make_response(jsonify({'status': 'link is none'}), 400)
    originalLink = bodyData.get('link')
    status, responseData = linkController.addNewLink(originalLink)
    return make_response(jsonify(responseData), status)


@links.route('', methods=['GET'])
def getShortURL():
    if not 'request_id' in request.args:
        return make_response(jsonify({'status': 'request_id is none'}), 400)
    requestId = request.args.get('request_id')
    print requestId
    status, responseData = linkController.getShortLink(requestId)
    return make_response(jsonify(responseData), 200)


@links.route('', methods=['DELETE'])
def deleteShortURL():
    if not request.data:
        return make_response(jsonify({'status': 'body data is none'}), 400)
    bodyData = convertDictToStr(
        jwt.decode(request.data, config.SECRET_KEY, algorithm=['HS256']))
    if not 'request_id' in bodyData:
        return make_response(jsonify({'status': 'request_id is none'}), 400)
    requestId = bodyData.get('request_id')
    status, responseData = linkController.deleteLink(requestId)
    return make_response(jsonify(responseData), status)
