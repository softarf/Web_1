"""
Django settings for hello project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))    # Можно и так.


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-bx9=er!0@**%5#-qi0hr=q+h^(^j_hon-2^-d5^m+s=&t$da65'

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

    # Здесь мы подключаем наши приложения
    'firstapp'
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

ROOT_URLCONF = 'hello.urls'

TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")    # Указывается путь на уровне папки конфигурации проекта.

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR, ],      # Здесь мы добавляем путь до шаблонов.
        # 'DIRS': [                    # Или так:
        #     os.path.join(BASE_DIR, "templates"),
        # ],
        'APP_DIRS': True,              # Так же, шаблоны можно разместить внутри приложений.
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

WSGI_APPLICATION = 'hello.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

# Здесь мы можем заменить настройки для другой БД, например PostgreSQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'firstapp_db.sqlite3',
        # Пример настроек для PostgreSQL.
        # 'ENGINE': 'django.db.backends.postgresql',
        # 'NAME': 'db_name',
        # 'USER': 'postgres',
        # 'PASSWORD': 'pass',
        # 'HOST': 'localhost',
        # 'PORT': 5432,
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

# Здесь мы можем заменить язык отображения Django и часовой пояс.
# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'ru-ru'               # Устанавливает русский язык для окна приветствия.

# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Yekaterinburg'      # Устанавливает местный часовой пояс.

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

# Назначает класс для ключей 'pk', создающихся в моделях проекта автоматически.
# Можно также объявить в 'firstapp/apps.py'.
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
