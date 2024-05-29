from django.apps import AppConfig


class TeamConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.contacts'
    verbose_name = "Контакты"
