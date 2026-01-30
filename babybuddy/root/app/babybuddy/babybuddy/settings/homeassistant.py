from .base import *
import os

ENABLE_HOME_ASSISTANT_SUPPORT = True
MESSAGE_STORAGE = "django.contrib.messages.storage.session.SessionStorage"

if os.getenv("CSRF_TRUSTED_ORIGINS"):
    CSRF_TRUSTED_ORIGINS = os.getenv("CSRF_TRUSTED_ORIGINS").split(",")
