# Generated by Django 3.0.5 on 2024-03-08 16:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('buku', '0004_buku_kategoriid'),
        ('koleksipribadi', '0003_auto_20240308_2237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='koleksipribadi',
            name='bukuid',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='buku.Buku'),
        ),
    ]
