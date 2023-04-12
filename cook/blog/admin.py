from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import *


class CustomMPTTModelAdmin(MPTTModelAdmin):
    mptt_level_indent = 20


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CustomMPTTModelAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post)
admin.site.register(Recipe)
admin.site.register(Comment)
