# Generated by Django 3.2.8 on 2021-10-27 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website_users', '0002_alter_familyprofile_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='familyprofile',
            name='family_name',
            field=models.TextField(max_length=15),
        ),
    ]
