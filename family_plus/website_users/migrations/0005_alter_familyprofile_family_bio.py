# Generated by Django 3.2.8 on 2021-10-29 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website_users', '0004_alter_familyprofile_family_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='familyprofile',
            name='family_bio',
            field=models.TextField(blank=True, default='Family bio has not been filled out.', null=True),
        ),
    ]