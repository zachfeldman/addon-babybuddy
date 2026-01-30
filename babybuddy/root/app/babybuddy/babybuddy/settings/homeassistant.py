from .base import *
import os

# Trust the headers passed by Ingress/Nginx
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
USE_X_FORWARDED_HOST = True
USE_X_FORWARDED_PORT = True

ENABLE_HOME_ASSISTANT_SUPPORT = True
MESSAGE_STORAGE = "django.contrib.messages.storage.session.SessionStorage"

if os.getenv("CSRF_TRUSTED_ORIGINS"):
    CSRF_TRUSTED_ORIGINS = os.getenv("CSRF_TRUSTED_ORIGINS").split(",")
