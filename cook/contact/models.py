from django.db import models
from ckeditor.fields import RichTextField


class ContactModel(models.Model):
    """Модель, отвечает за обратную связь"""
    name = models.CharField(max_length=50)
    email = models.EmailField()
    website = models.URLField(null=True, blank=True)
    message = models.TextField(max_length=5000)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.email}'


class ContactLink(models.Model):
    """Модель, отвечает за контакты"""
    icon = models.FileField(upload_to='icons/')
    name = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name}'


class About(models.Model):
    """Модель, отвечает за страницу о нас"""
    title = models.CharField(max_length=200)
    text = RichTextField()
    mini_text = RichTextField()


class ImageAbout(models.Model):
    """Модель, отвечает за изображения на странице о нас"""
    image = models.ImageField(upload_to='about/')
    page = models.ForeignKey(About, on_delete=models.CASCADE, related_name='about_images')


class Social(models.Model):
    """Модель, отвечает за соц сети страницы о нас """
    icon = models.FileField(upload_to='icons/')
    link = models.URLField()
    alt = models.CharField(max_length=100)