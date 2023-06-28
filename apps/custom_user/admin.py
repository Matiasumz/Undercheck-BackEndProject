from django.contrib import admin

# Register your models here.

from apps.custom_user.models import CustomUser
from django.contrib.auth.models import Permission


@admin.register(CustomUser)
class ClienteAdmin(admin.ModelAdmin):
    pass

admin.site.register(Permission)