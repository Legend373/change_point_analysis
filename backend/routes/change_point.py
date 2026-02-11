from flask import Blueprint, jsonify
from services.data_service import load_changepoints

changepoints_bp = Blueprint("changepoints", __name__)

@changepoints_bp.route("/")
def get_changepoints():
    return jsonify(load_changepoints())
