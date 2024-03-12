from django.db import models
from django.contrib.auth.models import User
from buku.models import Buku
from django.conf import settings
import uuid

# Create your models here.
class Koleksipribadi(models.Model):
    koleksiid = models.UUIDField(db_column='KoleksiID', primary_key=True, default=uuid.uuid4, editable=False)
    userid = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, db_column='UserID')
    bukuid = models.ForeignKey(Buku, on_delete=models.CASCADE, db_column='BukuID')

    def __str__(self):
        return f"{self.userid}'s Collection: {self.bukuid.judul}"
