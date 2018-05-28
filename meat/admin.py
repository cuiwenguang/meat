from django.contrib import admin
from django.contrib.auth.models import Permission


class PermissionAdmin(admin.ModelAdmin):
    list_filter = ('content_type__model',)

admin.site.register(Permission, PermissionAdmin)