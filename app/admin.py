from django.contrib import admin
from django.utils.translation import gettext_lazy as _
# from django.contrib.auth import get_user_model
from .models import User, Post

admin.site.register(User)
admin.site.register(Post)