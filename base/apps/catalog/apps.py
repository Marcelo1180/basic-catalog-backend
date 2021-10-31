from django.apps import AppConfig


class CatalogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'base.apps.catalog'

    def ready(self):
        import base.apps.catalog.signals

