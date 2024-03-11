from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin as BaseUseradmin
from django.contrib.auth.admin import UserChangeForm

from .models import User, Post

class UserAdmin(BaseUseradmin):
    form = UserChangeForm
    fieldsets = (
        (None, {'fields': ('email', 'password', )}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide', ),
            'fields': ('email', 'password'),
        }),
    )
    
    list_display = ['email', 'is_staff', 'is_active']
    search_fields = ['email']
    ordering = ['email']

admin.site.register(User, UserAdmin)
admin.site.register(Post)