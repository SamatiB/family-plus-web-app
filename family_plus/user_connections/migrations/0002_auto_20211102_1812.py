# Generated by Django 3.2.8 on 2021-11-03 01:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website_users', '0008_auto_20211029_2048'),
        ('user_connections', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='connectionslist',
            name='connections',
            field=models.ManyToManyField(blank=True, related_name='connections', to='website_users.FamilyProfile'),
        ),
        migrations.AlterField(
            model_name='connectionslist',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='users', to='website_users.familyprofile'),
        ),
        migrations.AlterField(
            model_name='connectrequest',
            name='receiver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to='website_users.familyprofile'),
        ),
        migrations.AlterField(
            model_name='connectrequest',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to='website_users.familyprofile'),
        ),
    ]