from django.db import models
from buku.models import Buku
from kategoribuku.models import Kategoribuku

class KategoribukuRelasi(models.Model):
    kategoribukuid = models.IntegerField(db_column='KategoriBukuID', primary_key=True)
    bukuid = models.ForeignKey(Buku, models.DO_NOTHING, db_column='BukuID')
    kategoriid = models.ForeignKey(Kategoribuku, models.DO_NOTHING, db_column='KategoriID')

    class Meta:
        managed = False
        db_table = 'kategoribuku_relasi'
