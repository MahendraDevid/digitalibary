from django.urls import path
from . import views

app_name = 'Kategoribuku'  # nama aplkasi

urlpatterns = [
    # Admin roles
    path('create/', views.create_Kategoribuku, name='create'),
    path('admin-petugas/list/', views.Kategoribuku_list, name='read'),
    path('update/<str:kategoriid>/', views.update_Kategoribuku, name='update'),
    path('delete/<str:kategoriid>/', views.delete_Kategoribuku, name='delete'),

    # Peminjam roles
    path('list/', views.Peminjam_Kategoribuku_list, name='kategori-read'),
    path('list/<int:kategori_id>/', views.lihat_buku_per_kategori, name='lihat_buku_per_kategori'),

]