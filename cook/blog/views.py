from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *


class HomeView(ListView):
    """Обработка главной страницы"""
    model = Post
    paginate_by = 6 # кол-во выводимых постов
    template_name = 'blog/home.html'

class PostListView(ListView):
    """Категория определенной статьи"""
    model = Post

    def get_queryset(self) -> list:
        """Фильтруем посты по нужной категории, переопределяем доступ к БД."""
        return Post.objects.filter(category__slug=self.kwargs['slug']).select_related('category')


class PostDetailView(DetailView):
    """Просмотр отдельного поста"""
    model = Post
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'





















