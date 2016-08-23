"""
Django settings for djangoecommerce project.

Generated by 'django-admin startproject' using Django 1.10.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os
import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'mu1hbq=$o@(qt=_skh#-@n*l4vbaz-1s0g6bm0wfd35ogv!yqq'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # JC: Início das apps de djangoecommerce
    'core',
    'catalog',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    # 'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'djangoecommerce.urls'

# Se houver mais de um arquivo, ele irá buscar o primeiro que encontrar na ordem:
# 1 = Nos diretórios extras de DIRS
# 2 = Dentro de cada aplicação de APP_DIRS, ordenado por INSTALLED_APPS
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # JC: DIRS é uma lista de diretórios aonde os templates devem estar
        'DIRS': [],
        # JC: APP_DIRS = True significa que o django irá procurar pelos templates dentro de uma pasta
        # template, dentro de cada aplicação.
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

WSGI_APPLICATION = 'djangoecommerce.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

# JC: Mudando o idioma para português do Brasil
LANGUAGE_CODE = 'pt-br'

# JC: Mudando o timezone para Recife
TIME_ZONE = 'America/Recife'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

# Todos os arquivos estáticos principais e comuns devem ficar no diretórios
# static da aplicação core, conforme padrão definido pelo nosso projeto
STATIC_URL = '/static/'
# Utilizando o STATICFILES_DIRS, bastaria criar o diretório 'staticfiles' na raíz do projeto
# que o Django iria encontrar todos os arquivos estáticos de dentro dela.
# STATICFILE_DIRS = [
#     os.path.join(BASE_DIR, 'staticfiles')
# ]

# Configurações para o heroku
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
ALLOWED_HOSTS = ['*']
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')

# Sobrescrevendo configurações definidas em arquivos locais específicos (produção e desenvolvimento)
try:
    from .local_settings import *
except ImportError:
    pass