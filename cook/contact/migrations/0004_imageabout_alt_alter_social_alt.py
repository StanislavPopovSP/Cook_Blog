# Generated by Django 4.2 on 2023-04-21 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_about_social_imageabout'),
    ]

    operations = [
        migrations.AddField(
            model_name='imageabout',
            name='alt',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='social',
            name='alt',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
