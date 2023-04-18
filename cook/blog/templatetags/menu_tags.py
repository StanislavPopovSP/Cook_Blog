from django import template
from blog.models import Category


register = template.Library()

@register.inclusion_tag('blog/include/tags/top_menu.html')
def get_categories():
    """Для вывода включающего тега"""
    # category = Category.objects.filter(parent__isnull=True).order_by('name')
    category = Category.objects.all()
    return {'list_category': category}