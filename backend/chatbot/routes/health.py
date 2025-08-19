from flask import Blueprint, jsonify

health_bp = Blueprint("health", name)

@health_bp.route("/health", methods=["GET"])``
def health():
return jsonify({"status": "ok"}), 200