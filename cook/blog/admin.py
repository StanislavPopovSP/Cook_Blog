from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import *


class CustomMPTTModelAdmin(MPTTModelAdmin):
    """Количество пикселей, для вложенных категорий"""
    mptt_level_indent = 20


# class CategoryAdmin(admin.ModelAdmin):
#     prepopulated_fields = {'slug': ('name',)}


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    """Регистрация и вывод нужных полей"""
    prepopulated_fields = {'slug': ('name',)}


class RecipeInline(admin.StackedInline):
    """Для соединения Рецептов с Постом"""
    model = Recipe
    extra = 1 # для вывода одного рецепта


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Регистрация и вывод нужных полей"""
    list_display = ['title', 'category', 'author', 'create_at', 'id']
    inlines = [RecipeInline] # подключение модели Recipe


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    """Регистрация и вывод нужных полей"""
    list_display = ['name', 'prep_time', 'cook_time', 'post']


admin.site.register(Category, CustomMPTTModelAdmin)
admin.site.register(Comment)
