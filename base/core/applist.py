# Application definition

DJANGO_APPS = (
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
)

LOCAL_APPS = (
    "base.apps.account",
    "base.apps.catalog",
)

THIRD_PARTY_APPS = (
    "rest_framework",
    "rest_framework.authtoken",
    "dj_rest_auth",
    "drf_yasg",
)


INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + THIRD_PARTY_APPS
