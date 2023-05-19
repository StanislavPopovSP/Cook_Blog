from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView, CreateView
from .models import *
from .forms import CommentForm, RegisterUserForm, LoginUserForm
from django.db.models import Q
from django.contrib.auth import login, logout, authenticate  # что бы авторизоваться автоматически
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required


class LoginUser(LoginView):
    """Авторизирует пользователя"""
    form_class = LoginUserForm
    template_name = 'users/login-register.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_login'] = LoginUserForm()
        context['error'] = 'Неверные данные для входа'
        return context


# def loginuser(request):
#     user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
#     if user is None:
#         return render(request, 'users/login-register.html',
#                       {'form_login': LoginUserForm(),
#                        'error': 'Неверные данные для входа'
#                        })  # Тогда мы пользователя должны перенаправить на страницу входа назад
#     else:
#         login(request, user)  # если пользователь есть, login() - он должен быть авторизирован, проверка на то что он есть
#         return redirect('home')

class RegisterUser(CreateView):
    """Регистрация пользователя, обработка формы"""
    form_class = RegisterUserForm
    template_name = 'users/login-register.html'

    def form_valid(self, form):
        """Переопределяем данный метод"""
        user = form.save()  # сохраняем форму и получаем пользователя
        login(self.request, user)  # после регистрации автоматически залогинились и перешли на страницу index
        return redirect('home')


@login_required
def logoutuser(request):
    """Функция, кнопки выхода из аккаунта."""
    if request.method == 'POST':  # Метод POST может быть только у элемента form
        logout(request)
        return redirect('home')


class OutputPosts(ListView):
    """Вывод на страницу регистрации постов"""
    model = Post
    template_name = 'users/login-register.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = RegisterUserForm()
        context['form_login'] = LoginUserForm()
        return context

    def get_queryset(self) -> list:
        """Вывод постов из всех категорий"""
        return Post.objects.filter(is_published=True).select_related('category')


class HomeView(ListView):
    """Обработка главной страницы"""
    model = Post
    paginate_by = 10  # кол-во выводимых постов
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
