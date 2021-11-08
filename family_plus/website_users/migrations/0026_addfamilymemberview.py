# Generated by Django 3.2.8 on 2021-11-08 21:17

from django.db import migrations, models
import django.db.models.deletion
import django.views.generic.edit


class Migration(migrations.Migration):

    dependencies = [
        ('website_users', '0025_alter_familymember_age_range'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddFamilyMemberView',
            fields=[
                ('familymember_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='website_users.familymember')),
            ],
            bases=(django.views.generic.edit.CreateView, 'website_users.familymember'),
        ),
    ]