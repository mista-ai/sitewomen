from django.contrib import admin
from .models import Women

class WomenAdmin(admin.ModelAdmin):
    list_display = ()

admin.site.register(Women)