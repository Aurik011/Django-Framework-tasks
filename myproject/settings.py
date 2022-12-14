"""
Django settings for myproject project.

Generated by 'django-admin startproject' using Django 3.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

# THIS IMPORT OS CODE BELOW WILL MAKE os WITHIN templates A VALD NAME -AURIK
import os # new      
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'w*3d6uexzikxu(vim!w5$0j08mhtaceapfec0_8-e3$jl@x_aq'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []
# Application definition

INSTALLED_APPS = [
    'myapp.apps.MyappConfig',
    'accounts.apps.AccountsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myproject',
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
ROOT_URLCONF = 'myproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        # 'DIRS': [r'C:\Users\octopus88\Desktop\myproject\myapp\templates'],  WORKS ONLY WHEN INSIDE MY APP, BUT GOOGLE SAYS, SAVE IT ON MYPROJECT  
        # THIS WORKS
        
        # 'DIRS': [os.path.join(BASE_DIR, 'templates')], NORMALLY THIS WAS HERE
        # 'DIRS': [os.path.join(BASE_DIR, 'templates/home.html')],  This does not work

        # 'DIRS': [os.path.join(SETTINGS_PATH, 'templates')], - found on web   
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

WSGI_APPLICATION = 'myproject.wsgi.application'
# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'myapp',
        'USER' : 'postgres',
        'PASSWORD' : '6024',
        'HOST' : 'localhost'

    }
}
# dataflair 
# DATABASES = {
# 'default': {
# 'ENGINE': 'django.db.backends.mysql',
# 'NAME': 'dataflair',
# 'USER': 'root',
# 'PASSWORD': '',
# 'HOST': '',
# 'PORT': '',
# 'OPTIONS': {
# 'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
# }
# }
# }

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'dataflair',
#         'USER': 'root',
#         'PASSWORD': ??????,
#         'HOST': ??????,
#         'PORT': ??????,
#         'OPTIONS': {
#              'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
# }
# }
# }


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/


STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'myproject/static')
]
STATIC_ROOT = os.path.join(BASE_DIR, 'assests')





