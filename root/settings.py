"""
2020 Black
Application settings configuration
developer : #ABS
"""

# Import all requirements
from pathlib import Path
import os
import locale


# SET PROJECT DIR
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SET BASE DIR
BASE_DIR = os.path.dirname(PROJECT_DIR)

# site id (for multi site enable)
SITE_ID = 1

# Application definition
INSTALLED_APPS = [
    # Django apps
    'django.contrib.staticfiles',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.auth',

    # Wagtail full
    'wagtail.contrib.modeladmin',
    'wagtail.contrib.redirects',
    'wagtail.contrib.forms',
    'wagtail.snippets',
    'wagtail.documents',
    'wagtail.embeds',
    'wagtail.sites',
    'wagtail.users',
    'wagtail.api.v2',
    'wagtail.images',
    'wagtail.search',
    'wagtail.admin',
    'wagtail',

    #allauth
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount',
    'allauth.account',
    'allauth',

    #External apps
    'rest_framework',
    'modelcluster',
    'jalali_date',
    'taggit',

    # Internal apps
    'index',
    'users',
    'blog',
    'product',
]


# MIDDLEWARE
MIDDLEWARE = [
    ''' Django MIDDLEWARE '''
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',

    ''' Wagtail MIDDLEWARE '''
    'wagtail.contrib.redirects.middleware.RedirectMiddleware',
]


# urls configuration
ROOT_URLCONF = 'root.urls'

# Templates configuration
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(Path(__file__).resolve().parent.parent, 'templates')],
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

# User authenticate backends
AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]

# User authenticate model
AUTH_USER_MODEL = 'users.CustomUser'

# WAGTAIL FRONTEND LOGIN TEMPLATE
WAGTAIL_FRONTEND_LOGIN_TEMPLATE = 'accounts/login.html'

# WAGTAIL FRONTEND LOGIN URL
WAGTAIL_FRONTEND_LOGIN_URL = '/accounts/login/'

# PASSWORD REQUIRED TEMPLATE
PASSWORD_REQUIRED_TEMPLATE = 'accounts/password_required.html'

# WSGI configuration
WSGI_APPLICATION = 'root.wsgi.application'

# Databases configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'YOUR_DB_NAME',
    }
}

'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'YOU_MYSQL_DB',
        'USER': 'YOU_MYSQL_DB_USER',
        'PASSWORD': 'YOU_MYSQL_DB_PASSWORD',
        'HOST': 'YOU_MYSQL_DB_HOST',
        'PORT': 'YOU_MYSQL_DB_PORT',
    }
}'''

# Internationalization configuration
LANGUAGE_CODE = 'fa'

TIME_ZONE = 'Asia/Tehran'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# STATIC FILES (CSS, JavaScript, Images)
STATICFILES_FINDERS = [
    ''' Run command : python3 manage.py collectstatic for collect STATIC FILES '''
    'django.contrib.staticfiles.finders.FileSystemFinder',

    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

# STATIC FILES DIRS
STATICFILES_DIRS = [
    os.path.join(PROJECT_DIR, 'static'),
]

# Manifest Static Files Storage is recommended in production, to prevent outdated
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

# static root Dir configuration
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# STATIC URL
STATIC_URL = '/static/'

# Media root Dir configuration
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# SERVER DEVELOPER configuration
ADMINS = [
    ('ADMINISTRATOR', 'UNIQUEADMINISTRATOR@UNIQUEDOMIL.com'),
]

''' !!! IMPORTAND !!! '''

# ADMINISTRATOR
MANAGERS = ADMINS

# SECRET KEY
SECRET_KEY = 'django-insecure-38n_&5$5ga9)#!-r$&jcyk3^v^673x0u3%f8)*4ekxrd$)=ujs'

# BASE ADMIN
WAGTAILADMIN_BASE_URL = ''

# ALLOWED HOSTS
ALLOWED_HOSTS = ['irabs174-verbose-happiness-g4q7p5vrgwwhwpp9-8000.preview.app.github.dev', '127.0.0.1', 'localhost']

# CSRF trusred origin
CSRF_TRUSTED_ORIGINS = ['https://irabs174-verbose-happiness-g4q7p5vrgwwhwpp9-8000.preview.app.github.dev']

# Default to dummy email backend. Configure dev/production/local backend
EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'

# Enail subject configuration
EMAIL_SUBJECT_PREFIX = '[Wagtail] '

# Internal IP Address configuration
INTERNAL_IPS = ('127.0.0.1', '10.0.2.2')

# logging configuration. The only tangible logging
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

# Brand name configuration
WAGTAIL_SITE_NAME = 'YOUR_DOMIN'

# Reverse the default case-sensitive handling of tags
TAGGIT_CASE_INSENSITIVE = True

# default persian calender settings (optional)
JALALI_DATE_DEFAULTS = {
   'Strftime': {
        'date': '%y/%m/%d',
        'datetime': '%H:%M:%S _ %y/%m/%d',
    },
    'Static': {
        'js': [
            # loading datepicker
            'admin/js/django_jalali.min.js',
            # OR
            # 'admin/jquery.ui.datepicker.jalali/scripts/jquery.ui.core.js',
            # 'admin/jquery.ui.datepicker.jalali/scripts/calendar.js',
            # 'admin/jquery.ui.datepicker.jalali/scripts/jquery.ui.datepicker-cc.js',
            # 'admin/jquery.ui.datepicker.jalali/scripts/jquery.ui.datepicker-cc-fa.js',
            # 'admin/js/main.js',
        ],
        'css': {
            'all': [
                'admin/jquery.ui.datepicker.jalali/themes/base/jquery-ui.min.css',
            ]
        }
    },
}

# LOGIN URL
LOGIN_URL = '/login/'

# LOGIN REDIRECT URL
LOGIN_REDIRECT_URL = '/'

# ACCOUNT AUTHENTICATION METHOD
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'

# ACCOUNT_CONFIRM_EMAIL_ON_GET
ACCOUNT_CONFIRM_EMAIL_ON_GET = False

# ACCOUNT_EMAIL_REQUIRED
ACCOUNT_EMAIL_REQUIRED = True

# ACCOUNT_USERNAME_REQUIRED
ACCOUNT_USERNAME_REQUIRED = False

# LOGIACCOUNT_EMAIL_VERIFICATIONN_URL
ACCOUNT_EMAIL_VERIFICATION = "none"

# LOGACCOUNT_LOGIN_ON_EMAIL_CONFIRMATIONIN_URL
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = False

# LOGIN_ACCOUNT_LOGOUT_ON_GET
ACCOUNT_LOGOUT_ON_GET = True

# ACCOUNT_LOGIN_ON_PASSWORD_RESET
ACCOUNT_LOGIN_ON_PASSWORD_RESET = True

# ACCOUNT_LOGOUT_REDIRECT_URL
ACCOUNT_LOGOUT_REDIRECT_URL = '/'

# ACCOUNT_PRESERVE_USERNAME_CASING
ACCOUNT_PRESERVE_USERNAME_CASING = False

# ACCOUNT_SESSION_REMEMBER 
ACCOUNT_SESSION_REMEMBER = True

# ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE 
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = False

# ACCOUNT_USERNAME_BLACKLIST
ACCOUNT_USERNAME_BLACKLIST = ["admin", 'security', 'secure', 'protection', 'safeguard',
 'privacy', 'confidential', 'shield', 'lock', 'encrypted', 'defender', 'guard', 'safety',
  'firewall', 'securex', 'sentinel', 'secureguard', 'securetech', 'cyber', 'hacker',
   'securecode', 'protect', 'securenet', 'securezone', 'securelock', 'securedata', 'securecloud',
    'securelink', 'secureaccess', 'securelogin', 'secureweb', 'accesscontrol', 'authentication',
     'authorization', 'biometric', 'cryptography', 'cybersecurity', 'dataprotection',
      'digitalcertificate', 'digitalsignature', 'end-to-endencryption', 'forensics',
       'identitymanagement', 'informationsecurity', 'integrity', 'intrusiondetection', 'malware',
        'networksecurity', 'password', 'phishing', 'ransomware', 'riskmanagement',
         'securityaudit', 'securitybreach', 'securityclearance', 'securitypolicy',
          'socialengineering','spyware', 'threatintelligence',
           'virus', 'vulnerabilityassessment', 'zeroday', "god"]

# ACCOUNT_USERNAME_MIN_LENGTH
ACCOUNT_USERNAME_MIN_LENGTH = 6

# Provider specific settings
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        # For each OAuth based provider, either add a ``SocialApp``
        # (``socialaccount`` app) containing the required client
        # credentials, or list them here:
        'APP': {
            'client_id': 'YOUR_CLIENT_ID',
            'secret': 'YOUR_SECRET',
        }
    }
}

# FORMS FOR AUTHENTICATION
ACCOUNT_FORMS = {
    ''' PLEASE KEEP THIS FILE SAFE !  '''
    'add_email': 'allauth.account.forms.AddEmailForm',
    'change_password': 'users.forms.CustomPasswordChangeForm',
    'disconnect': 'allauth.socialaccount.forms.DisconnectForm',
    'reset_password': 'allauth.account.forms.ResetPasswordForm',
    'reset_password_from_key': 'allauth.account.forms.ResetPasswordKeyForm',
    'set_password': 'allauth.account.forms.SetPasswordForm',
    'signup': 'users.forms.CustomUserCreationForm',
    'user_token': 'allauth.account.forms.UserTokenForm',
}

# Debug
DEBUG = True