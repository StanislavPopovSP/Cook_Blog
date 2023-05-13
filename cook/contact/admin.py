from django.contrib import admin
from .models import *


@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'create_at', 'id']
    list_display_links = ('name', 'email')
    list_filter = ('create_at',)


class ImageAboutInline(admin.StackedInline):
    """Для соединения фотографий со страницей о нас"""
    model = ImageAbout
    extra = 1


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    """Регистрация, вывод нужных полей соединение с ImageAbout"""
    list_display = ['title', 'id']
    inlines = [ImageAboutInline]


@admin.register(Social)
class AboutAdmin(admin.ModelAdmin):
    """Регистрация и вывод нужных полей"""
    list_display = ['link', 'icon', 'id']

@admin.register(ContactLink)
class ContactLinkAdmin(admin.ModelAdmin):
    list_display = ['name']