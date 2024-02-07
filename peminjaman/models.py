from django.db import models
from buku.models import Buku
from user.models import User

# Create your models here.
class Peminjaman(models.Model):
    peminjamanid = models.IntegerField(db_column='PeminjamanID', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey(User, models.DO_NOTHING, db_column='UserID')  # Field name made lowercase.
    bukuid = models.ForeignKey(Buku, models.DO_NOTHING, db_column='BukuID')  # Field name made lowercase.
    tanggalpeminjaman = models.DateField(db_column='TanggalPeminjaman')  # Field name made lowercase.
    tanggalpengembalian = models.DateField(db_column='TanggalPengembalian')  # Field name made lowercase.
    statuspeminjaman = models.CharField(db_column='StatusPeminjaman', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'peminjaman'