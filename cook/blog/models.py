from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey
from django.utils import timezone


class Category(MPTTModel):
    """Модель, отвечает за категории"""
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    parent = TreeForeignKey('self', related_name='children', on_delete=models.SET_NULL, null=True, blank=True)  # что бы были подкатегории

    def __str__(self):
        return self.name

    class MPTTMeta:
        """Автоматически упорядочивает элементы в дереве по ключу name"""
        order_insertion_by = ['name']


class Tag(models.Model):
    """Модель, отвечает за теги"""
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    """Модель, отвечает за пост"""
    author = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    slug = models.SlugField(max_length=200, unique=True, default='')
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='articles/%Y/%m/%d', null=True, blank=True)
    text = models.TextField()
    category = models.ForeignKey(Category, related_name='post', on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField(Tag, related_name='post', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    create_at = models.DateTimeField(auto_now_add=True)  # когда была создана данная запись

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """Конкретный путь для поста"""
        return reverse('post_single', kwargs={'slug': self.category.slug, 'post_slug': self.slug})

    def get_comments(self):
        """Доступ к комментариям"""
        return self.comment.all()


class Recipe(models.Model):
    """Модель, отвечает за рецепты"""
    name = models.CharField(max_length=100, null=True, blank=True)
    serves = models.CharField(max_length=50)
    prep_time = models.PositiveIntegerField(default=0)
    cook_time = models.PositiveIntegerField(default=0)
    ingredients = RichTextField()
    directions = RichTextField()
    post = models.ForeignKey(Post, related_name='recipes', on_delete=models.SET_NULL, null=True, blank=True)


class Comment(models.Model):
    """Модель, для комментариев"""
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    website = models.CharField(max_length=150, blank=True, null=True)
    message = models.TextField(max_length=500)
    create_at = models.DateTimeField(default=timezone.now)
    post = models.ForeignKey(Post, related_name='comment', on_delete=models.CASCADE)