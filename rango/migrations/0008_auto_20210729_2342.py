# Generated by Django 2.1.5 on 2021-07-29 22:42

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rango', '0007_userpofile'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserPofile',
            new_name='UserProfile',
        ),
    ]
