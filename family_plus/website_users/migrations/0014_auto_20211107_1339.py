# Generated by Django 3.2.8 on 2021-11-07 21:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('website_users', '0013_merge_0010_familymember_user_0012_auto_20211107_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='familyprofile',
            name='user',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='custom_user_model.customusermodel'),
        ),
        migrations.DeleteModel(
            name='FamilyMember',
        ),
    ]