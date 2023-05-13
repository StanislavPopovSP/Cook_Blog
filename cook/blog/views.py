from django.views.generic import ListView, DetailView, CreateView
from .models import *
from .forms import CommentForm
from django.db.models import Q


class HomeView(ListView):
    """Обработка главной страницы"""
    model = Post
    paginate_by = 4  # кол-во выводимых постов
    template_name = 'blog/home.html'

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
    paginate_by = 2

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
        return super().form_valid(form)

    def get_success_url(self):
        """Перенаправление на страницу поста"""
        return self.object.post.get_absolute_url()


# class Gallery(ListView):
#     template_name =