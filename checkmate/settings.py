"""
Django settings for checkmate project.
Generated by 'django-admin startproject' using Django 1.8.2.
"""

import os
import json

CONF_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(CONF_DIR)
CONF_DIR_NAME = os.path.relpath(CONF_DIR, BASE_DIR)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'so3h1n5^@g*!-d=f&)+-j+t7ze#qz9c3y#&xztnr^zjb5$&8cn'
DEBUG = True
ALLOWED_HOSTS = ['*']

# Other security settings
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
CSRF_COOKIE_HTTPONLY = True
X_FRAME_OPTIONS = 'DENY'

# Application definition

INSTALLED_APPS = (
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.staticfiles',
	'main',
)

MIDDLEWARE_CLASSES = (
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
	'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = CONF_DIR_NAME+'.urls'

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
			],
		},
	},
]

WSGI_APPLICATION = CONF_DIR_NAME+'.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

# Read from db.json, otherwise use default
try:
	with open(os.path.join(CONF_DIR, "db.json")) as _db_file:
		DATABASES = json.load(_db_file)
#		print("Using db.json for database settings")
except (FileNotFoundError, ValueError):
#	print("Using default SQLite db")
	DATABASES = {
		'default': {
			'ENGINE': 'django.db.backends.sqlite3',
			'NAME': os.path.join(BASE_DIR, 'sqlite3.db'),
		}
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR,'staticfiles')
STATICFILES_DIRS = (os.path.join(BASE_DIR,'static'),)


# Load configuration data
with open(os.path.join(BASE_DIR,'data','config.json')) as _config_file:
	CONFIG = json.load(_config_file)

# This will be used to indent all large JSON responses
if DEBUG:
	JSON_INDENT_LEVEL = 2
else:
	JSON_INDENT_LEVEL = None
# See this for indentation details:
# https://docs.python.org/3/library/json.html#json.dump
