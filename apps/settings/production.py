import dj_database_url
from .settings import *

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env('DB_NAME', default='db_project'),
        'USER': env('DB_USER', default='root'),
        'HOST': env('DB_HOST', default='localhost'),
        'PASSWORD': env('DB_PASSWORD', default=''),
        'PORT': env('DB_PORT', default=3306)
    }
}

DATABASES['default'] = dj_database_url.config()

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
