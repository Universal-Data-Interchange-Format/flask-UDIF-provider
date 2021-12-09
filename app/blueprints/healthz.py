from flask import Blueprint, jsonify

healthz = Blueprint('healthz', __name__)


@healthz.route('', methods=['GET'])
def get_health_check():

    return jsonify(dict(health="ok"))
