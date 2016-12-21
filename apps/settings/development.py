"""Development settings."""
from .settings import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env('DB_NAME', default='db_project'),
        'USER': env('DB_USER', default='root'),
        'HOST': env('DB_HOST', default='localhost'),
        'PASSWORD': env('DB_PASSWORD', default=''),
        'PORT': env('DB_PORT', default=3306)
    }
}
