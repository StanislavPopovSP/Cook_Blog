from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'slug', 'create_date', 'get_image', 'is_published', 'id']
    readonly_fields = ['get_image'] # что бы получать миниатюрку, что это за фотография

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="90" height="60"') # для html