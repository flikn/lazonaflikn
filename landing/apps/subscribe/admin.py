from django.contrib import admin
from .models import Subscriptor


class SubscriptorAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'client',
        'account',
        'date_created',
        'lifetime',
        'is_active',
    )
    list_filter = (
        'is_active',
    )

admin.site.register(Subscriptor, SubscriptorAdmin)
