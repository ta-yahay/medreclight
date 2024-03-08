"""
Django settings for medrec project.

Generated by 'django-admin startproject' using Django 4.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import os
from pickle import TRUE
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-pbin@9c@xaie3!956(dw5(gfu3-95n6d90nq4$xb==3e)'
# SECRET_KEY =os.environ.get('SECRET_KEY')
# SECURITY WARNING: don't run with debug turned on in production!
# SECRET_KEY = [os.environ['SECRET']]
# CSRF_TRUSTED_ORIGINS=['https://'+ os.environ['WEBSITE_HOSTNAME']]

DEBUG = True
ALLOWED_HOSTS =['https://'+ os.environ['WEBSITE_HOSTNAME']] if 'WEBSITE_HOSTNAME' in os.environ else []
CSRF_TRUSTED_ORIGINS = ['https://'+ os.environ['WEBSITE_HOSTNAME']]if 'WEBSITE_HOSTNAME' in os.environ else []

# ALLOWED_HOSTS = ['http://lab3ta.azurewebsites.net/',
#  'http://lab3ta.azurewebsites.net',
#  'lab3ta.azurewebsites.net/',
#  'lab3ta.azurewebsites.net','127.0.0.1']
# CSRF_TRUSTED_ORIGINS = ['http://lab3ta.azurewebsites.net/',
#  'http://lab3ta.azurewebsites.net',
#  'lab3ta.azurewebsites.net/',
#  'lab3ta.azurewebsites.net','127.0.0.1']


# ALLOWED_HOSTS =[os.environ['WEBSITE_HOSTNAME']]


# Application definition

INSTALLED_APPS = [
    'rest_framework',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    ## my apps
    'Patient',
    'Pages', 
    'Readings',
    'accounts',
    'bootstrap4',
    'crispy_forms',
    'django_filters',
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'medrec.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
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

WSGI_APPLICATION = 'medrec.wsgi.application'

# connection_string =os.environ['AZURE_POSTGRESQL_CONNECTIONSTRING']
# parameters={pair.split('='):pair.split('=')[1]for pair in connection_string.split(' ')}


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': parameters['dbname'],
#         'USER': parameters['user'],
#         'PASSWORD': parameters['password'],
#         'HOST': parameters['host'],
#     }
# } 
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "mydatabase",
    }
}


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'medrec',
#         'USER': 'postgres',
#         'PASSWORD': 'yahyakhalaf',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }


REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}




# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Static files (CSS, JavaScript, Images)

# https://docs.djangoproject.com/en/4.0/howto/static-files/
# STATIC_ROOT =os.path.join(BASE_DIR , 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_ROOT =BASE_DIR / 'staticfiles'
STATIC_URL = 'static/'

STATICFILES_DIRS=[
    os.path.join(BASE_DIR,'medrec/static')
]
    

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# media
MEDIA_ROOT =os.path.join(BASE_DIR , 'media')
MEDIA_URL = 'media/'




FILE_UPLOAD_HANDLERS = ("django_excel.ExcelMemoryFileUploadHandler",
                        "django_excel.TemporaryExcelFileUploadHandler")

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}
