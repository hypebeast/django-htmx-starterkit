"""
This file contains all the settings used in production.
This file is required and if development.py is present these
values are overridden.
"""

from config.settings.components import config

# Production flags:
# https://docs.djangoproject.com/en/3.2/howto/deployment/

DEBUG = False

ALLOWED_HOSTS = [
    # TODO: check production hosts
    config("DOMAIN_NAME"),
    # We need this value for `healthcheck` to work:
    "localhost",
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": config("POSTGRES_DB"),
        "USER": config("POSTGRES_USER"),
        "PASSWORD": config("POSTGRES_PASSWORD"),
        "HOST": config("DJANGO_DATABASE_HOST"),
        "PORT": config("DJANGO_DATABASE_PORT", cast=int),
        "CONN_MAX_AGE": config("CONN_MAX_AGE", cast=int, default=60),
        "OPTIONS": {
            "connect_timeout": 10,
            "options": "-c statement_timeout=15000ms",
        },
    },
}


# Staticfiles
# https://docs.djangoproject.com/en/4.1/ref/contrib/staticfiles/

# This is a hack to allow a special flag to be used with `--dry-run`
# to test things locally.
_COLLECTSTATIC_DRYRUN = config(
    "DJANGO_COLLECTSTATIC_DRYRUN",
    cast=bool,
    default=False,
)
# Adding STATIC_ROOT to collect static files via 'collectstatic':
STATIC_ROOT = ".static" if _COLLECTSTATIC_DRYRUN else "/var/www/django/static"

STATICFILES_STORAGE = (
    "django.contrib.staticfiles.storage.ManifestStaticFilesStorage"
)


# Media files
# https://docs.djangoproject.com/en/4.1/topics/files/

MEDIA_ROOT = "/var/www/django/media"


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

_PASS = "django.contrib.auth.password_validation"  # noqa: S105
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "{0}.UserAttributeSimilarityValidator".format(_PASS)},
    {"NAME": "{0}.MinimumLengthValidator".format(_PASS)},
    {"NAME": "{0}.CommonPasswordValidator".format(_PASS)},
    {"NAME": "{0}.NumericPasswordValidator".format(_PASS)},
]


# Security
# https://docs.djangoproject.com/en/4.1/topics/security/

SECURE_HSTS_SECONDS = 31536000  # the same as Caddy has
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SECURE_SSL_REDIRECT = True
SECURE_REDIRECT_EXEMPT = [
    # This is required for healthcheck to work:
    "^health/",
]

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
