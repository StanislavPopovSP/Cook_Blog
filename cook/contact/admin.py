from django.contrib import admin
from .models import *


@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'create_at', 'id']
    list_display_links = ('name', 'email')


class ImageAboutInline(admin.StackedInline):
    """Для соединения фотографий со страницей о нас"""
    model = ImageAbout
    extra = 1

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    """Регистрация и вывод нужных полей"""
    list_display = ['title', 'id']
    inlines = [ImageAboutInline]


admin.site.register(ContactLink)
admin.site.register(Social)