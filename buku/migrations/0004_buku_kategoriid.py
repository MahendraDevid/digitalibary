# Generated by Django 5.0.2 on 2024-03-04 04:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buku', '0003_alter_buku_options_buku_tersedia'),
        ('kategoribuku', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='buku',
            name='kategoriid',
            field=models.ForeignKey(db_column='KategoriID', default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='kategoribuku.kategoribuku'),
        ),
    ]
