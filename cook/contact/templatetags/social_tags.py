from django import template
from contact.models import Social

register = template.Library()


@register.simple_tag()
def get_social_links():
    """Включающий тег, вывод ссылок всех социальных сетей"""
    return Social.objects.all()
