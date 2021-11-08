# Generated by Django 3.2.8 on 2021-11-07 22:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website_users', '0018_remove_familymember_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='familymember',
            name='age_range',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='familymember',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='website_users.familyprofile'),
        ),
        migrations.AlterField(
            model_name='familymember',
            name='about',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='familymember',
            name='last_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]