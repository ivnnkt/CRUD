# Generated by Django 3.1.2 on 2021-06-08 22:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_profile_is_staff'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='is_staff',
            new_name='worker',
        ),
    ]