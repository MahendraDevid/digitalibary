from django.db import models
from kategoribuku.models import Kategoribuku

class Buku(models.Model):
    kategoriid = models.ForeignKey(Kategoribuku, models.DO_NOTHING, db_column='KategoriID', default=1)
    bukuid = models.IntegerField(db_column='BukuID', primary_key=True)
    judul = models.CharField(db_column='Judul', max_length=255)
    penulis = models.CharField(db_column='Penulis', max_length=255)
    penerbit = models.CharField(db_column='Penerbit', max_length=255)
    tahunterbit = models.IntegerField(db_column='TahunTerbit')
    tersedia = models.BooleanField(default=True)  # Menambahkan bidang 'tersedia'

    class Meta:
        db_table = 'buku'
        
    def __str__(self):
        return f"{self.kategoriid.namakategori}"
