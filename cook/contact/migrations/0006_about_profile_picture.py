# Generated by Django 4.2 on 2023-04-23 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0005_about_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='profile_picture',
            field=models.ImageField(default='user-default.png', upload_to='about/author_profile'),
        ),
    ]
