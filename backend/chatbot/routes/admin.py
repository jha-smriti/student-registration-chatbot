from flask import Blueprint, request, jsonify, current_app
from chatbot.schemas.admin import FAQCreateSchema

admin_bp = Blueprint("admin", name)

def _authorized(req) -> bool:
token = req.headers.get("Authorization", "").replace("Bearer ", "")
return token == current_app.config["ADMIN_TOKEN"]

@admin_bp.route("/admin/faqs", methods=["POST"])
def add_faq():
if not _authorized(request):
return jsonify({"error": "unauthorized"}), 401
data = request.get_json(force=True)
errors = FAQCreateSchema().validate(data)
if errors:
return jsonify({"error": errors}), 400
# Persistence will be added later
return jsonify({"status": "ok"}), 201