'''
Custom Users Database Model
'''

# Import all requirements
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.conf import settings
from django.core.cache import cache


# Custom User Manager class
class CustomUserManager(BaseUserManager):
    '''
    2020 BLACK USERS
    '''
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.has_new_password = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('has_new_password', True)
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    id = models.BigAutoField(db_column='id',primary_key=True, unique=True)
    email = models.CharField(db_column='email',max_length=120, unique=True, null=True)
    username = models.CharField(db_column='username',max_length=120, unique=True, null=True)
    WPOPass = models.CharField(db_column='WPOPass',max_length=100, default = False, null=True)
    full_name = models.CharField(db_column='full_name',max_length=255, null=True)
    is_active = models.BooleanField(db_column='is_active',default=True)
    collection = models.ForeignKey(
        'wagtailcore.Collection',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='یک مجموعه برای کاربر انتخاب کنید',
    )
    is_staff = models.BooleanField(db_column='is_staff',default=False)
    date_joined = models.DateTimeField(db_column='date_joined',auto_now_add=True)
    last_login = models.DateTimeField(db_column='last_login',auto_now_add=True)
    has_new_password = models.BooleanField(db_column='has_new_password',default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username',]

    objects = CustomUserManager()

    def __str__(self):
        try:
            return self.username
        except self.username.DoesNotExist:
            return self.email
            

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران سایت'
        
