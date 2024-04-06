from django.urls import path
from . import views

app_name = 'koleksipribadi'  # ganti dengan nama aplikasi Anda

urlpatterns = [
    path('list/', views.koleksipribadi_list, name='list'),
    path('create/<str:bukuid>/', views.create_koleksipribadi, name='create'),
    path('delete/<int:koleksi_id>/', views.delete_koleksipribadi_peminjam, name='delete'),

    # Admin List
    path('admin-list/', views.koleksipribadi_admin_list, name='list-admin'),
    path('delete/<int:koleksi_id>/', views.delete_koleksipribadi, name='delete_admin'),
]
