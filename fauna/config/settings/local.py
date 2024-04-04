from .base import *

import environ

env = environ.Env()

environ.Env.read_env(os.path.join(ROOT_DIR, ".env.local"))

SECRET_KEY = "django-insecure$@&^_)"

DEBUG = True

ALLOWED_HOSTS = ["*"]

CORS_ORIGIN_ALLOW_ALL = True


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env.str("POSTGRES_DB", default="fauna"),
        "USER": env.str("POSTGRES_USER", default="fauna"),
        "PASSWORD": env.str("POSTGRES_PASSWORD", default="fauna"),
        "HOST": env.str("POSTGRES_HOST", default="localhost"),
        "PORT": env.str("POSTGRES_PORT", default="5432"),
    }
}

REDIS_PASSWORD = env.str("REDIS_PASSWORD", default="ABCDE")
REDIS_HOST = env.str("REDIS_HOST", default="localhost")
REDIS_PORT = env.str("REDIS_PORT", default="6379")

REDIS_URL_PRE = f"redis://:{REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}"

CELERY_BROKER_URL = f"{REDIS_URL_PRE}/1"
CELERYBEAT_SCHEDULER = "django_celery_beat.schedulers:DatabaseScheduler"
CELERY_ENABLE_UTC = False
CELERY_TIMEZONE = "America/Bogota"
CELERY_RESULT_SERIALIZER = "json"
CELERY_TASK_SERIALIZER = "json"