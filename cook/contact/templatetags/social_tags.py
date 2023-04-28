from django import template
from contact.models import Social, About

register = template.Library()


@register.simple_tag()
def get_social_links():
    """Включающий тег, вывод ссылок всех социальных сетей"""
    return Social.objects.all()


@register.simple_tag()
def get_about():
    """Включающий тег, вывод изображения для left_nav.html, sidebar.html"""
    return About.objects.last()
