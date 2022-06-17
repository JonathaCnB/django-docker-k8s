from pathlib import Path

from decouple import config

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config("SECRET_KEY")

DEBUG = config("DEBUG", default=False, cast=bool)

ALLOWED_HOSTS = config("ALLOWED_HOSTS").split(" ")

INSTALLED_APPS = [
    # apps django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 3rd party
    'storages',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'django_k8s.urls'

CSRF_TRUSTED_ORIGINS = ['https://*.jonathacarlos.dev.br']

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'django_k8s.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

DB_USERNAME = config("POSTGRES_USER")
DB_PASSWORD = config("POSTGRES_PASSWORD")
DB_DATABASE = config("POSTGRES_DB")
DB_HOST = config("POSTGRES_HOST")
DB_PORT = config("POSTGRES_PORT")
DB_IS_AVAIL = all([
    DB_USERNAME,
    DB_PASSWORD,
    DB_DATABASE,
    DB_HOST,
    DB_PORT,

])
DB_READY = config("DB_READY", default=False, cast=bool)

DB_IGNORE_SSL = config("DB_IGNORE_SSL", default=False, cast=bool)

if DB_IS_AVAIL and DB_READY:
    DATABASES = {
        'default': {
            'ENGINE': config("DB_ENGINE"),
            'NAME': DB_DATABASE,
            'USER': DB_USERNAME,
            'PASSWORD': DB_PASSWORD,
            'HOST': DB_HOST,
            'PORT': DB_PORT
        }
    }
    if not DB_IGNORE_SSL:
        DATABASES['default']['OPTIONS'] = {
            "sslmode": 'require'
        }

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',  # noqa
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',  # noqa
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',  # noqa
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',  # noqa
    },
]

LANGUAGE_CODE = 'pt-BR'

TIME_ZONE = 'America/Manaus'

DATE_FORMAT = "d/m/Y"

DATETIME_FORMAT = "d/m/Y H:i"

DATETIME_INPUT_FORMATS = "d/m/Y H:i"

TIME_FORMAT = "G:i:s"

USE_I18N = True

USE_TZ = True

USE_THOUSAND_SEPARATOR = True

STATIC_URL = 'static/'

STATIC_ROOT = BASE_DIR / 'staticfiles-cdn'

STATICFILES_DIRS = [
    BASE_DIR / "staticfiles"
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

from .cdn.conf import *  # noqa
