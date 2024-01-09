# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

from config.settings.components import BASE_DIR

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
