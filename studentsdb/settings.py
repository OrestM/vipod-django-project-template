"""
Django settings for studentsdb project.

Generated by 'django-admin startproject' using Django 1.8.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

from django.conf import global_settings
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PORTAL_URL = 'http://localhost:8000'
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=%1*o-pmwddz-!o%0kxl0@6@d7ir4=#)xnl7_--gd4_o+3*1i+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
	'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
	'crispy_forms',
	'students',
)

CRISPY_TEMPLATE_PACK = 'bootstrap3'

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
	
)

ROOT_URLCONF = 'studentsdb.urls'

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
				"students.context_processors.groups_processor",				
            ],
        },
    },
]

WSGI_APPLICATION = 'studentsdb.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

from .db import DATABASES

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE='uk'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

# Portal url is in context_pocessors.py
# PORTAL_URL = 'http://localhost:8000'

TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + ("django.core.context_processors.request", "studentsdb.context_processors.students_proc", )

TEMPLATE_DIRS = (
	'C:/data/work/virtualenvs/studentsdb/src/studentsdb/students/templates/students',
)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, '..', 'media')

from .email import *

LOG_FILE = os.path.join(BASE_DIR, 'studentsdb.log')

LOGGING = {
	'version': 1,
	'disable_existing_loggers': True,
	'formatters': {
		'verbose': {
			'format': '%(levelname)s %(asctime)s %(module)s: $(message)s'
		},
		'simple': {
			'format': '%(levelname)s: %(message)s'			
		},
	},
	'handlers': {
		'null': {
			'level': 'DEBUG',
			'class': 'logging.NullHandler',
		},
		'console': {
			'level': 'INFO',
			'class': 'logging.StreamHandler',
			'formatter': 'verbose'
		},
		'file': {
			'level': 'INFO',
			'class': 'logging.FileHandler',
			'filename': LOG_FILE,
			'formatter': 'verbose'
		},
	},
	'loggers': {
		'django': {
			'handlers': ['null'],
			'propagate': True,
			'level': 'INFO',
		},
		'students.signals': {
			'handlers': ['console', 'file'],
			'level': 'INFO',
		},
		'ContactView.as_view()': {
			'handlers': ['console', 'file'],
			'level': 'INFO',
		}
	}
}