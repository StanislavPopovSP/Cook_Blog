from django.contrib import admin
from .models import *


@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'create_at', 'id']
    list_display_links = ('name', 'email')


admin.site.register(ContactLink)