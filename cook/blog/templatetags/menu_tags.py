from django import template
from blog.models import Category, Post

register = template.Library()


@register.inclusion_tag('blog/include/tags/top_menu.html')
def get_categories():
    """Включающий тег, вывод всех категорий и подкатегорий"""
    # category = Category.objects.filter(parent__isnull=True).order_by('name')
    category = Category.objects.all()
    return {'list_category': category}


@register.inclusion_tag('blog/include/tags/recipes_tag.html')
def get_last_posts():
    """Включающий тег, забираем пять последних постов"""
    posts = Post.objects.select_related('category').order_by('-id')[:5]
    return {'list_last_post': posts}