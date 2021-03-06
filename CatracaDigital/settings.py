from pathlib import Path

from decouple import config, Csv
from dj_database_url import parse as dburl

########################################################################
# Basic configuration
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default=[], cast=Csv())

########################################################################
# Application definition
DEFAULT_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = [
    'django_extensions',
    'test_without_migrations',
    'djangobower',
    'rest_framework',
]

LOCAL_APPS = [
    'CatracaDigital.core.apps.CoreConfig',
    'CatracaDigital.landing.apps.LandingConfig',
    'CatracaDigital.payment.apps.PaymentConfig',
    'CatracaDigital.api.apps.ApiConfig',
]

INSTALLED_APPS = DEFAULT_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'CatracaDigital.urls'

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

WSGI_APPLICATION = 'CatracaDigital.wsgi.application'

########################################################################
# Database
default_dburl = 'sqlite:///' + str(BASE_DIR.joinpath(BASE_DIR, 'db.sqlite3'))

DATABASES = {
    'default': config('DATABASE_URL', default=default_dburl, cast=dburl),
}

########################################################################
# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LOGIN_URL = '/core/login'

########################################################################
# Email configuration
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = config('EMAIL_HOST')
EMAIL_PORT = config('EMAIL_PORT', cast=int)
EMAIL_USE_TLS = config('EMAIL_USE_TLS', cast=bool)
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')

########################################################################
# Internationalization
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_L10N = True
USE_TZ = True
DATE_INPUT_FORMATS = '%d/%m/%Y',

########################################################################
# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = str(BASE_DIR.joinpath('staticfiles'))
STATICFILES_FINDER = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'djangobower.finders.BowerFinder',
]

BOWER_COMPONENTS_ROOT = str(BASE_DIR)
BOWER_INSTALLED_APPS = (
    "animate.css#3.5.1",
    "bootstrap#3.3.6",
    "flexslider#2.6.1",
    "jquery.fitvids#1.1.0",
    "jquery#2.2.4",
    "font-awesome#4.6.3",
    "isMobile#0.4.0",
    "protonet/jquery.inview#1.1.2",
    "matchHeight#0.7.0",
    "jquery-placeholder#2.3.1",
    "jquery.scrollTo#2.1.2",
    "jquery.easing#1.3.1",
    "eonasdan-bootstrap-datetimepicker#latest"
)

########################################################################
# API Credentials
GOOGLE_API_KEY = config("GOOGLE_API_KEY")