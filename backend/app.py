from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv

from chatbot.routes.chat import chat_bp
from chatbot.routes.admin import admin_bp
from chatbot.routes.health import health_bp

def create_app():
load_dotenv()
app = Flask(name)
app.config.from_object("config.Config")

CORS(app, resources={r"/api/*": {"origins": app.config["ALLOWED_ORIGINS"].split(",")}})

app.register_blueprint(chat_bp, url_prefix="/api")
app.register_blueprint(admin_bp, url_prefix="/api")
app.register_blueprint(health_bp, url_prefix="/")

return app
app = create_app()

if name == "main":
app.run(host="0.0.0.0", port=8000, debug=True)