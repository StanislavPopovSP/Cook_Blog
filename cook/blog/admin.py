from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import *


class CustomMPTTModelAdmin(MPTTModelAdmin):
    mptt_level_indent = 20


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'author', 'create_at', 'id']

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['name', 'prep_time', 'cook_time', 'post']


admin.site.register(Category, CustomMPTTModelAdmin)
admin.site.register(Comment)
