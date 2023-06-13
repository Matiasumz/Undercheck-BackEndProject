from django.contrib import admin

# Register your models here.

from apps.custom_user.models import CustomUser


@admin.register(CustomUser)
class ClienteAdmin(admin.ModelAdmin):
    pass