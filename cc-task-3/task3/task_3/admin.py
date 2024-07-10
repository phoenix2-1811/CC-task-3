

# Register your models here.
from django.contrib import admin
from .models import *


@admin.register(task)
class ProfileAdmin(admin.ModelAdmin):
    search_fields=["file_name"]