from django.urls import path
from . import views

urlpatterns = [
    path('daftar/', views.daftar_buku, name='daftar_buku'),
    path('tambah/', views.tambah_buku, name='tambah_buku'),
    path('ubah/<int:buku_id>/', views.ubah_buku, name='ubah_buku'),
    path('hapus/<int:buku_id>/', views.hapus_buku, name='hapus_buku'),
]
