from .base import INSTALLED_APPS, MIDDLEWARE, BASE_DIR


DEBUG = True

THIRD_PARTY_APPS = [
    'debug_toolbar',
]

INSTALLED_APPS += THIRD_PARTY_APPS


THIRD_PARTY_MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

MIDDLEWARE += THIRD_PARTY_MIDDLEWARE

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

INTERNAL_IPS = [
 "127.0.0.1",
]