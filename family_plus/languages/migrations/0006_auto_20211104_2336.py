# Generated by Django 3.2.8 on 2021-11-05 06:36

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('languages', '0005_auto_20211104_2018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='languagespecifier',
            name='afrikaans',
            field=models.ManyToManyField(blank=True, related_name='afrikaans', to=settings.AUTH_USER_MODEL, verbose_name='Afrikaans'),
        ),
        migrations.AlterField(
            model_name='languagespecifier',
            name='albanian',
            field=models.ManyToManyField(blank=True, related_name='albanian', to=settings.AUTH_USER_MODEL, verbose_name='Albanian'),
        ),
    ]
