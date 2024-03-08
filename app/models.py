from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser
from django.utils.translation import gettext_lazy as _
from datetime import date

class User(AbstractBaseUser):
    username = models.CharField(max_length=100)
    email = models.EmailField(_('email address'), unique = True)
    joinDate = date.today()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return "{}".format(self.email)
    
class Post(models.Model):
    author = (models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE))
    title = models.CharField(max_length=50)
    content = models.TextField()
    date = date.today()