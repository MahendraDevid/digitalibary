
from django.shortcuts import render, redirect, get_object_or_404
from .models import Kategoribuku
from buku.models import Buku
from .forms import KategoribukuForm
from django.forms import HiddenInput
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# FItur Peminjam
def Peminjam_Kategoribuku_list(request):
    kategoris = Kategoribuku.objects.all()
    return render(request, 'kategoribuku/peminjam_daftar_kategori.html', {'kategoris': kategoris})

def lihat_buku_per_kategori(request, kategori_id):
    kategori = Kategoribuku.objects.get(pk=kategori_id)
    bukus = Buku.objects.filter(kategoriid=kategori_id)
    return render(request, 'buku/peminjam_daftar_buku.html', {'kategori': kategori, 'bukus': bukus})

# FItur Admin
def Kategoribuku_list(request):
    kategoris = Kategoribuku.objects.all()
    return render(request, 'kategoribuku/daftar_kategori.html', {'kategoris': kategoris})

def create_Kategoribuku(request):
    if request.method == 'POST':
        form = KategoribukuForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Kategoribuku:read')
    else:
        form = KategoribukuForm()
    return render(request, 'kategoribuku/kategori_form.html', {'form': form})

def update_Kategoribuku(request, kategoriid):
    kategoribuku = get_object_or_404(Kategoribuku, kategoriid=kategoriid)  # Ganti Kategoribuku menjadi kategoribuku
    if request.method == 'POST':
        form = KategoribukuForm(request.POST, instance=kategoribuku)
        if form.is_valid():
            form.save()
            return redirect('Kategoribuku:read')
    else:
        form = KategoribukuForm(instance=kategoribuku)
        form.fields['kategoriid'].widget = HiddenInput()

    return render(request, 'kategoribuku/kategori_form.html', {'form': form})

def delete_Kategoribuku(request, kategoriid):
    kategoribuku = get_object_or_404(Kategoribuku, kategoriid=kategoriid)
    kategoribuku.delete()
    return redirect('Kategoribuku:read')

# Menghitung total data kategori
def total_data_kategori(request):
    total = Kategoribuku.objects.all().count()# Memanggil fungsi tanpa argumen
    return total

# FItur Petugas
def petugas_Kategoribuku_list(request):
    kategoris = Kategoribuku.objects.all()
    return render(request, 'kategoribuku/petugas_daftar_kategori.html', {'kategoris': kategoris})

def create_Kategoribuku_petugas(request):
    if request.method == 'POST':
        form = KategoribukuForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Kategoribuku:read_petugas')
    else:
        form = KategoribukuForm()
    return render(request, 'kategoribuku/petugas_kategori_form.html', {'form': form})

def update_Kategoribuku_petugas(request, kategoriid):
    kategoribuku = get_object_or_404(Kategoribuku, kategoriid=kategoriid)  # Ganti Kategoribuku menjadi kategoribuku
    if request.method == 'POST':
        form = KategoribukuForm(request.POST, instance=kategoribuku)
        if form.is_valid():
            form.save()
            return redirect('Kategoribuku:read_petugas')
    else:
        form = KategoribukuForm(instance=kategoribuku)
        form.fields['kategoriid'].widget = HiddenInput()

    return render(request, 'kategoribuku/petugas_kategori_form.html', {'form': form})

def delete_Kategoribuku_petugas(request, kategoriid):
    kategoribuku = get_object_or_404(Kategoribuku, kategoriid=kategoriid)
    kategoribuku.delete()
    return redirect('Kategoribuku:read_petugas')