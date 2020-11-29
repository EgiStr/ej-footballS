from django.contrib import admin

# Register your models here.
from .models import Costumer


class Admin(admin.ModelAdmin):
    readonly_field = ['publish']


admin.site.register(Costumer, Admin)
