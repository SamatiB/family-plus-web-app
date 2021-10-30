# Generated by Django 3.2.8 on 2021-10-30 03:48

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('website_users', '0007_familyprofile_hidden'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='familyprofile',
            name='hidden',
        ),
        migrations.AddField(
            model_name='familyprofile',
            name='hidden',
            field=models.ManyToManyField(related_name='toggled_profiles', to=settings.AUTH_USER_MODEL),
        ),
    ]