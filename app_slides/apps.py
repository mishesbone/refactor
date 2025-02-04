#app_slides/apps.py
from django.apps import AppConfig

class AppSlidesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_slides'
    verbose_name = 'Slides Management'
