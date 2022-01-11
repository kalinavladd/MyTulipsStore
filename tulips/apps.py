from django.apps import AppConfig


class TulipsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tulips'
    verbose_name = "Тюльпаны"
    """Меняем имя нашего приложения на главной странице админки, далее __init__.py"""
