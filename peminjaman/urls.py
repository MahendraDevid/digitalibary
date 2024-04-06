from django.urls import path
from . import views

app_name = 'Peminjaman'  # nama aplkasi

urlpatterns = [
    # Peminjam roles
    path('create/<str:bukuid>/', views.create_Peminjaman, name='create'),
    path('list/', views.Peminjaman_list, name='read'),

    # Admin roles
    path('admin/list/', views.admin_peminjaman_list, name='admin-read'),
    path('update/<str:peminjamanid>/', views.update_Peminjaman, name='update'),
    path('delete/<str:peminjamanid>/', views.delete_Peminjaman, name='delete'),
    path('laporan/<int:peminjaman_id>/', views.generate_laporan_peminjaman, name='generate_laporan_peminjaman'),
    
    # petugas roles
    path('petugas/list/', views.petugas_peminjaman_list, name='petugas-read'),
    path('petugas/update/<str:peminjamanid>/', views.update_Peminjaman_petugas, name='petugas-update'),
    path('petugas/delete/<str:peminjamanid>/', views.delete_Peminjaman_petugas, name='petugas-delete'),
]