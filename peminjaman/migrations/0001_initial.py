# Generated by Django 4.2 on 2024-02-07 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Peminjaman',
            fields=[
                ('peminjamanid', models.IntegerField(db_column='PeminjamanID', primary_key=True, serialize=False)),
                ('tanggalpeminjaman', models.DateField(db_column='TanggalPeminjaman')),
                ('tanggalpengembalian', models.DateField(db_column='TanggalPengembalian')),
                ('statuspeminjaman', models.CharField(db_column='StatusPeminjaman', max_length=50)),
            ],
            options={
                'db_table': 'peminjaman',
                'managed': False,
            },
        ),
    ]