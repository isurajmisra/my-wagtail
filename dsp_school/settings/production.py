from .base import *

DEBUG = False

ALLOWED_HOSTS = ['my-wagtail.herokuapp.com']

try:
    from .local import *
except ImportError:
    pass
