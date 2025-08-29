import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
 
 
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

GEOIP_PATH = os.path.join(BASE_DIR, 'geoip', 'GeoLite2-City.mmdb')

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-5+_3*broq@f@9$hro&cdfs4k^4obmci+hx+*=nxa(20fd24elq'

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
    'django_user_agents',
        'rest_framework',

          'corsheaders',

    'visitors',
    # 'django.contrib.gis',
    'animator',


]


 
 
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # يجب أن يكون في الأعلى
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # django_user_agents
    'django_user_agents.middleware.UserAgentMiddleware',

]

ROOT_URLCONF = 'project.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'project.wsgi.application'


# إضافة CORS
# INSTALLED_APPS += ['corsheaders']
# MIDDLEWARE = ['corsheaders.middleware.CorsMiddleware'] + MIDDLEWARE
 


CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
]

# إعدادات الوسائط
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# import os
# from pathlib import Path

# # تحديد مسار المشروع
# BASE_DIR = Path(__file__).resolve().parent.parent

# # إعدادات ملفات الاستاتيكية
# STATIC_URL = '/static/'

# STATICFILES_DIRS = [
#     BASE_DIR / "static",  # تأكد من وجود هذا المجلد
# ]

# STATIC_ROOT = BASE_DIR / 'staticfiles'  # تأكد من وجود هذا المجلد

# # إعدادات ملفات الوسائط
# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# # باقي الإعدادات

# DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# إعدادات الوسائط
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),  # تأكد من وجود هذا المجلد
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # تأكد من وجود هذا المجلد

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'