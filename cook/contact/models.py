from django.db import models
from ckeditor.fields import RichTextField


class ContactModel(models.Model):
    """Модель, отвечает за обратную связь"""
    name = models.CharField(max_length=50, verbose_name='Имя отправителя')
    email = models.EmailField()
    website = models.URLField(null=True, blank=True)
    message = models.TextField(max_length=5000, verbose_name='Сообщение')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return f'{self.name} - {self.email}'

    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная связь'


class ContactLink(models.Model):
    """Модель, отвечает за контакты"""
    icon = models.FileField(upload_to='icons/', verbose_name='Иконка')
    name = models.CharField(max_length=200, verbose_name='Адрес, телефон, email')

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'


class About(models.Model):
    """Модель, отвечает за страницу о нас"""
    name = models.CharField(max_length=50, default='', verbose_name='Имя шев повара')
    profile_picture = models.ImageField(upload_to='about/author_profile', default='user-default.png', verbose_name='Фото профиля')
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    text = RichTextField(verbose_name='Описание об авторе')
    mini_text = RichTextField(verbose_name='Текст меню слайдера')
    max_text = RichTextField(default='', verbose_name='Текст на странице поста')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'

    # Как альтернатива запросу шаблона
    # def get_first_image(self):
    #     """Получает первую фотографию"""
    #     item = self.about_images.first()
    #     return item.image.url

    # Как альтернатива запросу шаблона
    # def get_image(self):
    #     """Возвращается со второго изображения"""
    #     return self.about_images.order_by('id')[1:4]

class ImageAbout(models.Model):
    """Модель, отвечает за изображения на странице о нас"""
    image = models.ImageField(upload_to='about/', verbose_name='Изображение')
    page = models.ForeignKey(About, on_delete=models.CASCADE, related_name='about_images')
    alt = models.CharField(max_length=100, null=True, blank=True, verbose_name='seo_name')


class Social(models.Model):
    """Модель, отвечает за соц сети страницы о нас """
    icon = models.FileField(upload_to='icons/', verbose_name='Изображение иконки')
    link = models.URLField(verbose_name='Ссылка для связи')
    alt = models.CharField(max_length=100, null=True, blank=True, verbose_name='seo_name')

    class Meta:
        verbose_name = 'Соц сети'
        verbose_name_plural = 'Соц сети'