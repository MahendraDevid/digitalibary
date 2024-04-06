from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    # Path untuk login dan register
    path('login/', views.Login.as_view(), name='login'),
    path('admin/login/', views.LoginAdmin.as_view(), name='login_admin'),
    path('petugas/login/', views.LoginPetugas.as_view(), name='login_petugas'),
    path('admin/register/', views.register_admin, name='register_admin'),
    path('register/', views.register, name='register'),
    path('logout/', views.user_logout, name='logout'),
    
    # Path untuk dashboard
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('petugas-dashboard/', views.petugas_dashboard, name='petugas_dashboard'),
    path('peminjam-dashboard/', views.peminjam_dashboard, name='peminjam_dashboard'),
    
    # path untuk user
    path('list/', views.user_list, name='user_list'),
]

