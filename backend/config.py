import os

class Config:
SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret")
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/chatbot")
REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")
ALLOWED_ORIGINS = os.getenv("ALLOWED_ORIGINS", "http://localhost:5173")
CONF_THRESHOLD = float(os.getenv("CONF_THRESHOLD", "0.6"))
ADMIN_TOKEN = os.getenv("ADMIN_TOKEN", "change-me")
SMS_BASE_URL = os.getenv("SMS_BASE_URL", "")
SMS_API_KEY = os.getenv("SMS_API_KEY", "")