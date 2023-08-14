from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import *

@admin.register(Category)
class CustomMPTTModelAdmin(MPTTModelAdmin, admin.ModelAdmin):
    """Количество пикселей, для вложенных категорий и настройка вывода элементов"""
    mptt_level_indent = 20
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'id']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    """Настройка тегов"""
    prepopulated_fields = {'slug': ('name',)}


class RecipeInline(admin.StackedInline):
    """Для соединения Рецептов с Постом"""
    model = Recipe
    extra = 1 # для вывода одного рецепта


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Настройка админ панели поста"""
    prepopulated_fields = {'slug': ('title',)}
    list_display = ['title', 'category', 'author', 'create_at', 'is_published', 'id']
    search_fields = ('title',)
    inlines = [RecipeInline] # подключение модели Recipe
    list_editable = ['is_published']  # для того что бы поле было кликабельным, например для галочек
    list_filter = ('is_published', 'create_at')  # фильтр полей
    save_as = True # сохраняет как новый объект, уже существующий
    save_on_top = True # кнопки сохранения будут вверху


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    """Настройка админ панели рецептов"""
    list_display = ['name', 'prep_time', 'cook_time', 'post', 'id']
    list_display_links = ('name', 'post')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """Настройка админ панели комментариев"""
    list_display = ['name', 'email', 'website', 'create_at', 'id']
    list_filter = ('create_at',)