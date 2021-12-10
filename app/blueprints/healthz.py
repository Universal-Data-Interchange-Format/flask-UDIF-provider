from flask import Blueprint, jsonify
from app.celery import celery_health_check

healthz = Blueprint('healthz', __name__)


@healthz.route('', methods=['GET'])
def get_health_check():
    result = celery_health_check.apply_async()
    if result.get():
        return jsonify(dict(server="running", celery='running'))
    else:
        return jsonify(dict(server="running", celery='bad'))
