"""
2020 Black
developer : #ABS
"""

# Import all requirements
from django.apps import AppConfig


# blog app config
class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
