"""
Django settings for Braydons_Horror_house project.

Generated by 'django-admin startproject' using Django 4.2.10.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
from pathlib import Path
import os
import dj_database_url

import cloudinary
from dotenv import load_dotenv


if os.path.isfile('env.py'):
    import env

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['8000-mlal83-braydonshorrorho-la272tzjoud.ws-eu114.gitpod.io',
                 '8000-mlal83-braydonshorrorho-xaa7lat3x30.ws-eu110.gitpod.io',
                 '8000-mlal83-braydonshorrorho-o0luur7727l.ws-eu108.gitpod.io',
                 '8000-mlal83-braydonshorrorho-o0luur7727l.ws-eu110.gitpod.io',
                 '8000-mlal83-braydonshorrorho-92nd3i24k7b.ws-eu114.gitpod.io',
                 '8000-mlal83-braydonshorrorho-o0luur7727l.ws-eu109.gitpod.io',
                 '8000-mlal83-braydonshorrorho-k1z7jh4hic2.ws.codeinstitute-ide.net', 
                 '.herokuapp.com', 
                 'braydons-horror-house-5e9401912ad6.herokuapp.com',
                 ]
                
CSRF_TRUSTED_ORIGINS = [
     'https://8000-mlal83-braydonshorrorho-la272tzjoud.ws-eu114.gitpod.io',
     'https://8000-mlal83-braydonshorrorho-o0luur7727l.ws-eu110.gitpod.io',
     'https://8000-mlal83-braydonshorrorho-o0luur7727l.ws-eu111.gitpod.io',
     'https://8000-mlal83-braydonshorrorho-92nd3i24k7b.ws-eu114.gitpod.io', 
     'https://8000-mlal83-braydonshorrorho-xaa7lat3x30.ws-eu110.gitpod.io',
     'https://8000-mlal83-braydonshorrorho-k1z7jh4hic2.ws.codeinstitute-ide.net',
]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cloudinary_storage',
    'crispy_forms',
    'crispy_bootstrap5',
    'django_summernote',
    'cloudinary',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'stories',
]

SITE_ID = 1
LOGIN_REDIRECT_URL = '/stories/'
LOGOUT_REDIRECT_URL = '/stories/'

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'Braydons_Horror_house.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
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

WSGI_APPLICATION = 'Braydons_Horror_house.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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

ACCOUNT_EMAIL_VERIFICATION = 'none'

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

CLOUDINARY_URL = os.environ.get("CLOUDINARY_URL")

APPEND_SLASH = False 


# Media settings
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
MEDIA_URL = '/media/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
