from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    # Path untuk login dan register
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('register/', views.register, name='register'),
    
    # Path untuk dashboard
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('petugas-dashboard/', views.petugas_dashboard, name='petugas_dashboard'),
    path('peminjam-dashboard/', views.peminjam_dashboard, name='peminjam_dashboard'),
]

