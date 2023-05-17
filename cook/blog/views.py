from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView, CreateView
from .models import *
from .forms import CommentForm
from django.db.models import Q


# def login_user(request):
#     return render(request, 'users/login-register.html')


class HomeView(ListView):
    """Обработка главной страницы"""
    model = Post
    paginate_by = 10  # кол-во выводимых постов
    template_name = 'blog/home.html'

    def get_queryset(self) -> list:
        """Вывод постов из всех категорий"""
        return Post.objects.filter(is_published=True).select_related('category')

class ViewElement(ListView):
    """Вывод на страницу постов"""
    model = Post
    paginate_by = 10
    template_name = 'users/login-register.html'
    context_object_name = 'posts'

    def get_queryset(self) -> list:
        """Вывод постов из всех категорий"""
        return Post.objects.filter(is_published=True).select_related('category')

class Search(ListView):
    """Поиск постов на главной странице"""
    template_name = 'blog/base.html'

    def get_queryset(self) -> list:
        return Post.objects.distinct().filter(
            Q(title__icontains=self.request.GET.get('search_query')) |
            Q(text__icontains=self.request.GET.get('search_query'))
        )


class PostListView(ListView):
    """Категория определенной статьи"""
    model = Post
    paginate_by = 4


    def get_queryset(self) -> list:
        """Фильтруем опубликованные посты по нужной категории, переопределяем доступ к БД"""
        return Post.objects.filter(category__slug=self.kwargs['slug'], is_published=True).select_related('category')


class PostDetailView(DetailView):
    """Просмотр отдельного поста, вывод формы"""
    model = Post
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context


class CreateComment(CreateView):
    """Обрабатывает форму для создания комментария """
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        """Привязка комментария к посту"""
        form.instance.post_id = self.kwargs.get('pk')
        self.object = form.save()
        return redirect(self.object.post.get_absolute_url())

    # def get_success_url(self):
    #     """Перенаправление на страницу поста"""
    #     return self.object.post.get_absolute_url()