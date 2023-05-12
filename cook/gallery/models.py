from django.db import models

class Photo(models.Model):
    """Модель, отвечает за фотографии"""
    name = models.CharField(max_length=250, blank=True, null=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)
    image = models.ImageField(upload_to='gallery/%Y/%m/%d')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name'] # сортировка по имени