# Generated by Django 3.0.5 on 2024-03-08 16:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('buku', '0004_buku_kategoriid'),
        ('peminjaman', '0007_auto_20240308_2248'),
    ]

    operations = [

    ]
