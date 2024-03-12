from django.urls import path
from . import views

app_name = 'Peminjaman'  # nama aplkasi

urlpatterns = [
    # Peminjam roles
    path('create/<str:bukuid>/', views.create_Peminjaman, name='create'),
    path('list/', views.Peminjaman_list, name='read'),
    path('update/<str:peminjamanid>/', views.update_Peminjaman, name='update'),
    path('delete/<str:peminjamanid>/', views.delete_Peminjaman, name='delete'),

    # Admin roles
    path('admin-petugas/list/', views.admin_peminjaman_list, name='admin-read'),
    path('laporan/<int:peminjaman_id>/', views.generate_laporan_peminjaman, name='generate_laporan_peminjaman'),
]