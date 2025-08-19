import os
import redis

_redis = None

def _get_client():
global _redis
if _redis is None:
_redis = redis.from_url(os.getenv("REDIS_URL", "redis://localhost:6379/0"))
return _redis

def cache_get(key):
try:
return _get_client().get(key)
except Exception:
return None

def cache_set(key, value, ex=3600):
try:
_get_client().set(key, value, ex=ex)
except Exception:
pass