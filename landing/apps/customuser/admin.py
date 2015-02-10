from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from utils.actions import export_as_excel
from .models import MyUser


class MyUserAdmin(admin.ModelAdmin):
    actions = (
        export_as_excel,
    )
    list_display = (
        'id',
        'email',
        'first_name',
        'last_name',
        'username',
        'last_login',
        'is_admin',
        'was_registered',
        'was_subscribed',
        'raw_password',
        'subscriptor',
    )
    list_filter = (
        'is_admin',
        'was_registered',
        'was_subscribed',
    )
    fieldsets = (
        (None, {'fields': (
            'username',
            'email',
            'password',
            'raw_password',
            'was_registered',
            'was_subscribed',
            'subscriptor',
        )}),
        ('Personal info', {'fields': (
            'first_name',
            'last_name',
            'last_login',
        )}),
        ('Permissions', {'fields': (
            'is_admin',
        )}),
    )
    search_fields = (
        'username',
        'email',
        'first_name',
        'last_name',
    )
    ordering = (
        'email',
    )

admin.site.register(MyUser, MyUserAdmin)
