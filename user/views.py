from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import RegistrationForm
from django.contrib.auth.models import Group
from user.models import User
from django.contrib.auth import logout

class Login(LoginView):
    template_name = 'registration/login.html'  

    def get_success_url(self):
        user = self.request.user
        if user.is_authenticated:
            if user.groups.filter(name='Petugas').exists():
                return reverse('petugas_dashboard')  # Ganti 'staff_dashboard' dengan nama URL untuk dashboard petugas
            elif user.groups.filter(name='Peminjam').exists():
                return reverse('peminjam_dashboard')  # Ganti 'borrower_dashboard' dengan nama URL untuk dashboard peminjam
            elif user.groups.filter(name='Admin').exists():
                return reverse('admin_dashboard')  # Ganti 'admin_dashboard' dengan nama URL untuk dashboard administrator
        return super().get_success_url()
    
class LoginAdmin(LoginView):
    template_name = 'registration/login_admin.html'  

    def get_success_url(self):
        user = self.request.user
        if user.is_authenticated:
            if user.groups.filter(name='Petugas').exists():
                return reverse('petugas_dashboard')  # Ganti 'staff_dashboard' dengan nama URL untuk dashboard petugas
            elif user.groups.filter(name='Peminjam').exists():
                return reverse('peminjam_dashboard')  # Ganti 'borrower_dashboard' dengan nama URL untuk dashboard peminjam
            elif user.groups.filter(name='Admin').exists():
                return reverse('admin_dashboard')  # Ganti 'admin_dashboard' dengan nama URL untuk dashboard administrator
        return super().get_success_url()
    
class LoginPetugas(LoginView):
    template_name = 'registration/login_petugas.html'  

    def get_success_url(self):
        user = self.request.user
        if user.is_authenticated:
            if user.groups.filter(name='Petugas').exists():
                return reverse('petugas_dashboard')  # Ganti 'staff_dashboard' dengan nama URL untuk dashboard petugas
            elif user.groups.filter(name='Peminjam').exists():
                return reverse('peminjam_dashboard')  # Ganti 'borrower_dashboard' dengan nama URL untuk dashboard peminjam
            elif user.groups.filter(name='Admin').exists():
                return reverse('admin_dashboard')  # Ganti 'admin_dashboard' dengan nama URL untuk dashboard administrator
        return super().get_success_url()

# Dashboard
@login_required
def admin_dashboard(request):
    # Logika tampilan dashboard administrator
    return render(request, 'dashboard/admin_dashboard.html')

@login_required
def petugas_dashboard(request):
    # Logika tampilan dashboard petugas
    return render(request, 'dashboard/petugas_dashboard.html')

@login_required
def peminjam_dashboard(request):
    # Logika tampilan dashboard peminjam
    return render(request, 'dashboard/peminjam_dashboard.html')

def register_admin(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            admin_group = Group.objects.get(name='Admin')
            user.groups.add(admin_group)
            return redirect('login')  # Ganti 'login' dengan nama URL untuk halaman login
    else:
        form = RegistrationForm()
    return render(request, 'registration/register_admin.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            peminjam_group = Group.objects.get(name='Peminjam')
            user.groups.add(peminjam_group)
            return redirect('login')  # Ganti 'login' dengan nama URL untuk halaman login
    else:
        form = RegistrationForm(initial={'role': 'peminjam'})  # Set default role to 'Peminjam'
    return render(request, 'registration/register_peminjam.html', {'form': form})


# Fungsi untuk logout
def user_logout(request):
    logout(request)
    return redirect('login')  # Ganti 'login' dengan nama URL untuk halaman login jika diperlukan

@login_required
def user_list(request):
    users = User.objects.all()
    return render(request, 'registration/user_list.html', {'users': users})

# Fungsi total data user
def total_data_user():
    total = User.objects.all().count()
    return total  # Mengembalikan total tanpa menggunakan dictionary