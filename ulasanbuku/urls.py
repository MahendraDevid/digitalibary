from django.urls import path
from . import views

app_name = 'ulasanbuku'

urlpatterns = [
    path('create/<int:bukuid>/', views.create_ulasan, name='create'),
    path('update/<int:ulasanid>/', views.update_ulasan_peminjam, name='update'),
    path('delete/<int:ulasanid>/', views.delete_ulasan_peminjam, name='delete'),
    path('list/', views.ulasan_list, name='list'),
    path('view/<int:bukuid>/', views.view_ulasan, name='view'),
    
    # list admin
    path('admin-list/', views.ulasan_admin_list, name='list-admin'),
    path('admin/update/<int:ulasanid>/', views.update_ulasan, name='update_admin'),
    path('admin/delete/<int:ulasanid>/', views.delete_ulasan, name='delete_admin'),
    
    
]
