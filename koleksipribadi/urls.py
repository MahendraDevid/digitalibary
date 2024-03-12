from django.urls import path
from . import views

app_name = 'koleksipribadi'  # ganti dengan nama aplikasi Anda

urlpatterns = [
    path('list/', views.koleksipribadi_list, name='list'),
    path('create/<str:bukuid>/', views.create_koleksipribadi, name='create'),
    path('delete/<uuid:koleksi_id>/', views.delete_koleksipribadi, name='delete'),

]
