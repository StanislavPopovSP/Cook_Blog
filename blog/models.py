from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey
from django.utils import timezone


class Category(MPTTModel):
    """Модель, отвечает за категории"""
    name = models.CharField(max_length=100, verbose_name='Название категории')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='URL')
    parent = TreeForeignKey('self', related_name='children', on_delete=models.SET_NULL, null=True, blank=True)  # что бы были подкатегории

    def __str__(self):
        return self.name

    class MPTTMeta:
        """Автоматически упорядочивает элементы в дереве по ключу name"""
        order_insertion_by = ['name']

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Tag(models.Model):
    """Модель, отвечает за теги"""
    name = models.CharField(max_length=100, verbose_name='Название тега')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='URL')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

class Post(models.Model):
    """Модель, отвечает за пост"""
    author = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE, verbose_name='Пользователь')
    slug = models.SlugField(max_length=200, unique=True, default='', verbose_name='URL')
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    image = models.ImageField(upload_to='articles/%Y/%m/%d', null=True, blank=True, verbose_name='Изображение')
    text = models.TextField(verbose_name='Описание')
    category = models.ForeignKey(Category, related_name='post', on_delete=models.SET_NULL, null=True, verbose_name='Категория')
    tags = models.ManyToManyField(Tag, related_name='post', blank=True, verbose_name='Теги')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')  # когда была создана данная запись

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def get_absolute_url(self):
        """Конкретный путь для поста"""
        return reverse('post_single', kwargs={'slug': self.category.slug, 'post_slug': self.slug})

    def get_comments(self):
        """Доступ к комментариям"""
        return self.comment.all()


class Recipe(models.Model):
    """Модель, отвечает за рецепты"""
    name = models.CharField(max_length=100, null=True, blank=True, verbose_name='Название рецепта')
    serves = models.CharField(max_length=50, verbose_name='Кол-во персон')
    prep_time = models.PositiveIntegerField(default=0, verbose_name='Время подготовки')
    cook_time = models.PositiveIntegerField(default=0, verbose_name='Время приготовления')
    ingredients = RichTextField(verbose_name='Ингредиенты')
    directions = RichTextField(verbose_name='Рецепт приготовления')
    post = models.ForeignKey(Post, related_name='recipes', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Пост')

    def __str__(self):
        return f'{self.post}'

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

class Comment(models.Model):
    """Модель, для комментариев"""
    name = models.CharField(max_length=50, verbose_name='Имя отправителя')
    email = models.CharField(max_length=100)
    website = models.CharField(max_length=150, blank=True, null=True)
    message = models.TextField(max_length=500, verbose_name='Сообщение')
    create_at = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')
    post = models.ForeignKey(Post, related_name='comment', on_delete=models.CASCADE, verbose_name='Пост')

    def __str__(self):
        return f'{self.post}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'