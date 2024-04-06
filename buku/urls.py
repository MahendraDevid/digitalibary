from django.urls import path
from . import views

app_name = 'buku'

urlpatterns = [
    
    #Admin Roles
    path('admin/list/', views.list_buku_admin, name='list_admin'),
    path('create/', views.create_buku, name='create'),
    path('update/<int:buku_id>/', views.update_buku, name='update'),
    path('delete/<int:buku_id>/', views.delete_buku, name='delete'),
    
    # Peminjam roles
    path('list/', views.list_buku_peminjam, name='list_peminjam'),
    
    # Petugas Roles
    path('petugas/list/', views.list_buku_petugas, name='list_petugas'),
    path('petugas/create/', views.create_buku_petugas, name='create_petugas'),
    path('petugas/update/<int:buku_id>/', views.update_buku_petugas, name='update_petugas'),
    path('petugas/delete/<int:buku_id>/', views.delete_buku_petugas, name='delete_petugas'),
    
]
