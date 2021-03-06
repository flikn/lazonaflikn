import os
import dj_database_url


BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', ' ')

# SECURITY WARNING: don't run with debug turned on in production!
# Default mode is set to False
DEBUG = bool(os.environ.get('DEBUG', False))

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '*').split()


# Grappelli customization
GRAPPELLI_ADMIN_TITLE = 'la zona flikn'

# Application definition

INSTALLED_APPS = (
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social.apps.django_app.default',
    'apps.subscribe',
    'apps.home',
    'apps.customuser',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'landing.middleware.SocialAuthExceptionMiddleware',
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

LANGUAGE_CODE = 'es'

TIME_ZONE = 'America/Lima'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Static files (CSS, JavaScript, Images)
STATIC_ROOT = os.environ.get(
    'STATIC_ROOT', os.path.join(BASE_DIR, 'staticfiles')
)
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
)

# Static files.

STATIC_URL = '/static/'

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.request",
    "social.apps.django_app.context_processors.backends",
    "social.apps.django_app.context_processors.login_redirect",
)

TEMPLATE_LOADERS = (
    ('django.template.loaders.cached.Loader', (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )),
)

if DEBUG:
    TEMPLATE_LOADERS = TEMPLATE_LOADERS[0][1]

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

# Custom User Model
AUTH_USER_MODEL = 'customuser.MyUser'
SOCIAL_AUTH_USER_MODEL = AUTH_USER_MODEL
DEFAULT_AUTHENTICATION_BACKEND = 'apps.customuser.backends.EmailBackend'

# Python social auth.
AUTHENTICATION_BACKENDS = (
    'social.backends.facebook.FacebookAppOAuth2',
    'social.backends.facebook.FacebookOAuth2',
    'social.backends.twitter.TwitterOAuth',
    'apps.customuser.backends.EmailBackend',
    'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/subscribe/'
LOGIN_URL = '/login/'

SOCIAL_AUTH_TWITTER_KEY = os.environ.get(
    'SOCIAL_AUTH_TWITTER_KEY', ' '
)
SOCIAL_AUTH_TWITTER_SECRET = os.environ.get(
    'SOCIAL_AUTH_TWITTER_SECRET', ' '
)

SOCIAL_AUTH_FACEBOOK_KEY = os.environ.get(
    'SOCIAL_AUTH_FACEBOOK_KEY', ' '
)
SOCIAL_AUTH_FACEBOOK_SECRET = os.environ.get(
    'SOCIAL_AUTH_FACEBOOK_SECRET', ' '
)
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']

SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'apps.customuser.pipeline.associate_by_email_or_username',
    'social.pipeline.user.get_username',
    'apps.customuser.pipeline.require_extra_data',
    'apps.customuser.pipeline.create_user',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details',
)
