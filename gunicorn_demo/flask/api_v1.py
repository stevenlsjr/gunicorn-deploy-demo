from flask import Blueprint, request, jsonify, make_response, helpers
from .db import get_db, get_poll_service
import logging
api_v1 = Blueprint('api', __name__, url_prefix='/api/v1')
logger = logging.getLogger(__name__)

@api_v1.route('/', methods=('GET',))
def index():
    return jsonify({
        'routes': [
            {"polls": request.host_url + 'api/v1/polls/'}
        ]
    })

@api_v1.route('/polls/', methods=('GET',))
def comments_list():
    if request.method == 'GET':
        limit = request.args.get('limit', 50)
        offset = request.args.get('offset', 0)
        try:
           limit = int(limit)
           offset = int(offset)
        except ValueError:
            return helpers.BadRequest(f'limit "{limit}" and offset "{offset}" must be integers')
        polls = get_poll_service().list(limit=limit, offset=offset)
        return jsonify({
            'limit': limit,
            'offset': offset,
            'results': polls
        })
    else:
        raise NotImplementedError()


@api_v1.route('/polls/<int:id>/', methods=('GET',))
def comments_detail(id):
    if request.method == 'GET':
        poll = get_poll_service().get(id=id)
        return jsonify(poll)
    else:
        raise NotImplementedError()

    