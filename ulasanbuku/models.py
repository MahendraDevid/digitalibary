from django.db import models
from buku.models import Buku
from user.models import User

class Ulasanbuku(models.Model):
    ulasanid = models.AutoField(db_column='UlasanID', primary_key=True)  # Menggunakan CharField untuk ID ulasan
    userid = models.ForeignKey(User, on_delete=models.CASCADE, db_column='UserID', default=1)
    bukuid = models.ForeignKey(Buku, on_delete=models.CASCADE, db_column='BukuID', default=1)
    ulasan = models.TextField(db_column='Ulasan')
    rating = models.IntegerField(db_column='Rating')

    class Meta:
        db_table = 'ulasanbuku'

    def save(self, *args, **kwargs):
        if not self.ulasanid:
            last_id = Ulasanbuku.objects.order_by('ulasanid').last()
            if last_id:
                last_id_number = last_id.ulasanid + 1
            else:
                last_id_number = 1
            self.ulasanid = last_id_number
        super().save(*args, **kwargs)
