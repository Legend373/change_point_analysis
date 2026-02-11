from flask import Blueprint, jsonify
from services.data_service import load_events

events_bp = Blueprint("events", __name__)

@events_bp.route("/")
def get_events():
    return jsonify(load_events())
