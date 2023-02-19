from django.contrib import admin
from . import models


# Register your models here.
class EventAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']


admin.site.register(models.ContactUs, EventAdmin)
