from django.shortcuts import render
from django.views.generic import ListView
from .models import *


class PostListView(ListView):
    """Категория определенной статьи"""
    model = Post

    def get_queryset(self) -> list:
        """Фильтруем посты по нужной категории, переопределяем доступ к БД."""
        return Post.objects.filter(category__slug=self.kwargs['slug']).select_related('category')

def home(request):
    return render(request, 'base.html')
