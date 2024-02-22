from django.db import models

class Buku(models.Model):
    bukuid = models.IntegerField(db_column='BukuID', primary_key=True)
    judul = models.CharField(db_column='Judul', max_length=255)
    penulis = models.CharField(db_column='Penulis', max_length=255)
    penerbit = models.CharField(db_column='Penerbit', max_length=255)
    tahunterbit = models.IntegerField(db_column='TahunTerbit')
    tersedia = models.BooleanField(default=True)  # Menambahkan bidang 'tersedia'

    class Meta:
        db_table = 'buku'
