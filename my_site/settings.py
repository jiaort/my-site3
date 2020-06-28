# -*- coding: UTF-8 -*-

"""
Django settings for my_site project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)

from __future__ import absolute_import
import os
from django.utils.termcolors import colorize
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'p-2_9jdgcawck*piav1d(kq-!((g#8#riop01(^5ilnl6f(ram'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
ALLOWED_HOSTS = ['*']
LOGIN_URL = '/manager/login/'

# Application definition

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bootstrap_pagination',
    'article',
)

MIDDLEWARE = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'utils.dlibs.middleware.request_init.RequestInitMiddleware',
)
# 在Django 3.0.x中XFrameOptionsMiddleware中间件设置X_FRAME_OPTIONS的默认值从SAMEORIGIN更改为DENY
X_FRAME_OPTIONS = 'SAMEORIGIN'

ROOT_URLCONF = 'my_site.urls'

WSGI_APPLICATION = 'my_site.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

MYSQLDB_CONNECT_TIMEOUT = 1
DATABASES = {
    'default': {
        'CONN_MAX_AGE': 3600,
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'my_site3',
        'USER': 'personal',
        'PASSWORD': 'qwer1234',
        'HOST': '172.17.0.1',
        'PORT': '3306',
        'TEST': {
            'CHARSET': 'utf8',
            'COLLATION': 'utf8_general_ci'
        },
        'OPTIONS': {
            'connect_timeout': MYSQLDB_CONNECT_TIMEOUT,
            'charset': 'utf8mb4'
        }
    }
}

# session设置
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
SESSION_EXPIRE_AT_BROWSER_CLOSE = False   # 是否将session有效期设置为到浏览器关闭为止
SESSION_COOKIE_AGE = 24 * 60 * 60  # 当上例为False时，此项生效，单位为秒
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://172.17.0.1:6379/1',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            'PASSWORD': '',
            'CONNECTION_POOL_KWARGS': {
                'max_connections': 100
            },
        }
    },
}

# celery config
from config.celery_conf import *

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False

LANGUAGES = (
    ('en', ('English')),
    ('zh-hans', ('中文简体')),
    # ('zh-hant', ('中文繁體')),
)

# 翻译文件所在目录，需要手工创建
LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

ADMINS = {('jiaort', 'heavycross@163.com')}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.csrf",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# import local settings
try:
    from .local_settings import *
    print(colorize(text='local_settings imported.', fg='yellow'))
except ImportError:
    pass
