"""
Django settings for dj_authentication project.

Generated by 'django-admin startproject' using Django 2.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'e+0h4vm*hwj092i92+l49uz-uta3g+pzbn@u%db4mk4nqs2*_('

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
    'apps.app_authenciate',
    'captcha',
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

ROOT_URLCONF = 'dj_authentication.urls'
BROKER_URL = 'redis://127.0.0.1:6379/2'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'dj_authentication.wsgi.application'
AUTH_USER_MODEL = 'app_authenciate.User'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dj_authentication',
        'USER':'root',
        'PASSWORD':'123456',
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS=(
    os.path.join(BASE_DIR,'static'),
)


#必须项
EMAIL_HOST = 'smtp.163.com'     #邮箱smtp服务地址
EMAIL_PORT = 25             #邮箱服务端口号
EMAIL_HOST_USER = 'jingyetong@163.com'   #发送的邮箱账号
EMAIL_HOST_PASSWORD = 'jinye123'     #授权码

#选填
# EMAIL_USE_TLS = True     #是否使用TLS安全设置
# DEFAULT_FROM_EMAIL = EMAIL_HOST_USER    #  默认发送用户
# CONFIRM_DAY=7         #有效时间




CACHES = {          #把缓存保存到Redis数据库
    "default": {
        # 使用redis做缓存
        'BACKEND': 'django_redis.cache.RedisCache',
        # 将缓存的数据保存在该目录下
        # 缓存的地址
        'LOCATION': 'redis://127.0.0.1:6379/15',
        # rediss: //[:password]@localhost:6379 / 0
        'TIMEOUT': 300,
        'OPTIONS': {
            # "PASSWORD": ""
            # 是否压缩缓存数据
            # "COMPRESSOR": "django_redis.compressors.zlib.ZlibCompressor",
            # 配置连接池
            "CONNECTION_POOL_KWARGS": {"max_connections": 100, "retry_on_timeout": True}
        }
    },
}