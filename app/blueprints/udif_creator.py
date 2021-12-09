import subprocess

from flask import Blueprint, jsonify
from flask import g, request
from celery import Celery

udif_creator = Blueprint('udif_creator', __name__)


@udif_creator.route('', methods=['GET'])
def create_udif_file():
    print(request.get_json())
    query = """select id, file_url from users_upload"""
    result = g.session.execute(query)
    for (id, file_url) in result:
        print(id, file_url)
    print(result)
    subprocess.call('run.bat')
    return jsonify(dict(health="ok"))


def completed_udif_creator():

    return jsonify(dict(health="ok"))