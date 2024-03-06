from django.db import models
from buku.models import Buku
from user.models import User

# Create your models here.
class Peminjaman(models.Model):
    DIPINJAM = 'Dipinjam'
    DIKEMBALIKAN = 'Dikembalikan'

    STATUS_CHOICES = [
        (DIPINJAM, 'Dipinjam'),
        (DIKEMBALIKAN, 'Dikembalikan'),
    ]

    peminjamanid = models.AutoField(db_column='PeminjamanID', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey(User, models.DO_NOTHING, db_column='UserID', default=1)  # Field name made lowercase.
    bukuid = models.ForeignKey(Buku, models.DO_NOTHING, db_column='BukuID', default=1)  # Field name made lowercase.
    tanggalpeminjaman = models.DateField(db_column='TanggalPeminjaman')  # Field name made lowercase.
    tanggalpengembalian = models.DateField(db_column='TanggalPengembalian')  # Field name made lowercase.
    statuspeminjaman = models.CharField(choices=STATUS_CHOICES, db_column='StatusPeminjaman', max_length=50)  # Field name made lowercase.
    
    class Meta:
        db_table = 'peminjaman'
        
    