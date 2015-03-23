import os
import dj_database_url
from configurations import Settings


class Base(Settings):
    USER_NAME = os.environ.get('USER', '')
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    ALLOWED_HOSTS = []

    INSTALLED_APPS = (
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'installer_profile',
        'installer_config',
    )

    MIDDLEWARE_CLASSES = (
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    )

    ROOT_URLCONF = 'installer.urls'
    WSGI_APPLICATION = 'installer.wsgi.application'

    DATABASES = {
            'default': dj_database_url.config(
                default='postgres://{}:@localhost:5432/installer'.format(USER_NAME))
        }

    LANGUAGE_CODE = 'en-us'
    TIME_ZONE = 'America/Los_Angeles'

    USE_I18N = True
    USE_L10N = True
    USE_TZ = True

    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(BASE_DIR, "static")
    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, "installer/static/"),
        )

    TEMPLATE_DIRS = (
        os.path.join(BASE_DIR, "installer/templates/"),
        )


class Dev(Base):
    DEBUG = True
    TEMPLATE_DEBUG = DEBUG
    SECRET_KEY = 'secret'


class Prod(Base):
    DEBUG = False
    TEMPLATE_DEBUG = DEBUG
    SECRET_KEY = os.environ.get('SECRET_KEY')