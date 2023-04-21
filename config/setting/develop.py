from config.settings import *

SECRET_KEY = 'django-insecure-&xqu-y6sbe4sf+1)x23*c$zyf2jsorcr+o@dw=2!4#fe&b-=l2'

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR/'/static'
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR/'media/'
STATICFILES_DIRS = [
    BASE_DIR/'static',
]

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'