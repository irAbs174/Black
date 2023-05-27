'''
Applications configuration
'''

# Import all requirements
from django.apps import AppConfig


# Applications configuration Class
class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
