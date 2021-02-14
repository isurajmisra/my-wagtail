from __future__ import absolute_import, unicode_literals
from .base import *
import dj_database_url
import os

DEBUG = False

env = os.environ.copy()
SECRET_KEY = env["SECRET_KEY"]
DATABASES["default"] = dj_database_url.config()

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

ALLOWED_HOSTS = ['my-wagtail.herokuapp.com']

try:
    from .local import *
except ImportError:
    pass
