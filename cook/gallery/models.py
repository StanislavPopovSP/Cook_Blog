from django.db import models

class Photo(models.Model):
    """Модель, отвечает за фотографии"""
    name = models.CharField(max_length=250, blank=True, null=True, verbose_name='Название изображения')
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True, verbose_name='URL')
    image = models.ImageField(upload_to='gallery/%Y/%m/%d', verbose_name='Изображение')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Фотография превью'
        verbose_name_plural = 'Фотография превью'
        ordering = ['name'] # сортировка по имени