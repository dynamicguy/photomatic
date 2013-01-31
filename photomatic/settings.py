# Django settings for photomatic project.
import os, sys
from datetime import timedelta
from os.path import abspath, dirname, basename, join
import dj_database_url
import djcelery

try:
    import social_auth
except ImportError:
    import sys

    sys.path.insert(0, '..')

ENV = (os.uname()[0] == 'Darwin') and 'development' or 'production'

DEBUG = (ENV == "development") and True or False
TEMPLATE_DEBUG = DEBUG

ROOT_PATH = abspath(dirname(dirname(__file__)))
PROJECT_NAME = basename(ROOT_PATH)

ADMINS = (
    ('Nurul Ferdous', 'nurul@ferdo.us'),
    )

MANAGERS = ADMINS

if(ENV == "development"):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'photomatic_development',
            'USER': 'ferdous',
            'PASSWORD': 'f',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }

else:
    DATABASES = {'default': dj_database_url.config()}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = False

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = join(ROOT_PATH, 'media/')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'
ADMIN_MEDIA_PREFIX = '/static/admin/'

# Additional locations of static files
STATICFILES_DIRS = (
    join(ROOT_PATH, 'static'),
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    )

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.DefaultStorageFinder',
    )

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'qp1^77u4m5mh=ut_3r%8lh)9$92rdufg7!4dn=0j^k4mr%$o4f'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
    )
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
    )

ROOT_URLCONF = 'photomatic.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'photomatic.wsgi.application'

TEMPLATE_DIRS = (
    join(ROOT_PATH, 'templates'),
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    )

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'kombu.transport.django',
    'djcelery',
    'social_auth',
    'photomatic',
    'fts',
    )

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

djcelery.setup_loader()
CELERY_RESULT_BACKEND = "mongodb"
CELERY_MONGODB_BACKEND_SETTINGS = {
    "host": "127.0.0.1",
    "port": '27017',
    "database": "photomatic",
    "taskmeta_collection": "my_taskmeta" # Collection name to use for task output
}
CELERYD_LOG_LEVEL = "INFO"
CELERY_AMQP_TASK_RESULT_EXPIRES = 18000  # 5 hours.

BROKER_BACKEND = "mongodb"
BROKER_HOST = "localhost"
BROKER_PORT = 27017
BROKER_USER = ""
BROKER_PASSWORD = ""
CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'
CELERY_IMPORTS = ('photomatic.tasks',)
CELERYBEAT_SCHEDULE = {
    'runs-every-50-seconds': {
        'task': 'photomatic.tasks.album_task',
        'schedule': timedelta(seconds=50),
        'args': None
    },
}

CELERY_TIMEZONE = 'UTC'

FACEBOOK_APP_ID = '497837306933727'
FACEBOOK_API_SECRET = '78411ecbe57c188c9d56686f11f7f6ef'
FACEBOOK_EXTENDED_PERMISSIONS = ['email', 'user_photos']

AUTHENTICATION_BACKENDS = (
    'social_auth.backends.facebook.FacebookBackend',
    'django.contrib.auth.backends.ModelBackend',
    )

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    'social_auth.context_processors.social_auth_by_type_backends')

#TEMPLATE_CONTEXT_PROCESSORS = (
#    'django.contrib.auth.context_processors.auth',
#    'django.core.context_processors.debug',
#    'django.core.context_processors.i18n',
#    'django.core.context_processors.media',
#    'django.contrib.messages.context_processors.messages',
#    'social_auth.context_processors.social_auth_by_type_backends',
#    )

try:
    from local_settings import *
except:
    pass
