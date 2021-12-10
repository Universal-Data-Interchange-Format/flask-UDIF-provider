from flask import Blueprint, jsonify
from flask import request

from app.celery import celery_process_udif

udif_creator = Blueprint('udif_creator', __name__)


@udif_creator.route('/create', methods=['GET'])
def create_udif_file():
    json_data = request.get_json()
    if json_data is None:
        return jsonify({'Error': 'user_id, username, requested_datetime are required.'})
    if 'user_id' not in json_data:
        return jsonify({'Error': 'user_id is required'})
    if 'username' not in json_data:
        return jsonify({'Error': 'username is required'})
    if 'requested_datetime' not in json_data:
        return jsonify({'requested_datetime': 'user_id is required'})

    user_id = json_data['user_id']
    username = json_data['username']
    requested_datetime = json_data['requested_datetime']
    try:
        celery_process_udif.delay(user_id, username, requested_datetime)
        return jsonify({"result": "Job is running. Once it been completed, it will send you file url."})
    except Exception as e:
        return jsonify({"result": f"Internal Error, {e.__str__()}"})


@udif_creator.route('/done', methods=['GET'])
def test_done():
    return jsonify({'result': 'Success'})
