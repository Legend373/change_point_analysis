from flask import Blueprint, jsonify
from services.data_service import load_prices

prices_bp = Blueprint("prices", __name__)

@prices_bp.route("/")
def get_prices():
    return jsonify(load_prices())
