from .base import *
import dj_database_url


DEBUG = False


DATABASES["default"] = dj_database_url.config()
ALLOWED_HOSTS = ['my-wagtail.herokuapp.com']

try:
    from .local import *
except ImportError:
    pass
