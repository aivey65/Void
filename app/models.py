from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, UserManager
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import PermissionsMixin
from datetime import date

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=100)
    email = models.EmailField(_('email address'), unique = True)
    joinDate = date.today()
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return "{}".format(self.email)
    
class Post(models.Model):
    author = (models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE))
    title = models.CharField(max_length=50)
    content = models.TextField(blank=True, null=True)
    date = models.DateField(auto_now_add=True)