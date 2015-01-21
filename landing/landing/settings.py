import os
import dj_database_url


BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', ' ')

# SECURITY WARNING: don't run with debug turned on in production!
# Default mode is set to False
DEBUG = bool(os.environ.get('DEBUG', False))

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS').split()


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'landing.urls'

WSGI_APPLICATION = 'landing.wsgi.application'

# Database
if DEBUG:
    DATABASES = {
        'default': dj_database_url.config(
            default='sqlite:///%s' % os.path.join(BASE_DIR, 'db.sqlite3'),
        ),
    }
else:
    DATABASES = {
        'default': dj_database_url.config(
            default=os.environ.get('POSTGRES_URL'),
        ),
    }

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
