# Generated by Django 4.2 on 2023-05-12 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_comment_create_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='Опубликовано'),
        ),
    ]
