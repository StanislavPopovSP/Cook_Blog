from django import template
from blog.models import Category, Post
from django.db.models import Count  # Считает кол-во элементов

register = template.Library()


def get_all_categories():
    """Возвращает все категории и кол-во постов в категории"""
    return Category.objects.annotate(Count('post'))


@register.simple_tag()
def get_list_category():
    """Считает количество постов в категории"""
    return get_all_categories()


@register.inclusion_tag('blog/include/tags/top_menu.html')
def get_categories():
    """Вывод всех категорий и подкатегорий, считает количество постов в категории"""
    # category = Category.objects.filter(parent__isnull=True).order_by('name')
    category = get_all_categories()
    return {'list_category': category}


@register.inclusion_tag('blog/include/tags/recipes_tag.html')
def get_last_posts():
    """Включающий тег, забираем пять последних постов"""
    posts = Post.objects.select_related('category').order_by('-id')[:20]
    return {'list_last_post': posts}


# @register.inclusion_tag('blog/include/tags/search_model.html')
# def search_profiles(request):
#     """Поиск постов"""
#     search_query = ''
#
#     if request.GET.get('search_query'):  # если пользователь что-то введет search_query, будет True.
#         search_query = request.GET.get('search_query')
#
#     post = Post.objects.distinct().filter(
#         title__icontains=search_query
#     )
#
#     return {'post': post, 'search_query': search_query}
