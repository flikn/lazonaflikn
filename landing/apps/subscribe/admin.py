from django.contrib import admin
from utils.actions import export_as_excel
from .models import Subscriptor


class SubscriptorAdmin(admin.ModelAdmin):
    actions = (
        export_as_excel,
    )
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
