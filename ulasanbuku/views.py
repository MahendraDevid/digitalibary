from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Ulasanbuku
from buku.models import Buku
from .forms import UlasanBukuForm

@login_required
def create_ulasan(request, bukuid):
    buku = get_object_or_404(Buku, pk=bukuid)
    if request.method == 'POST':
        form = UlasanBukuForm(request.POST)
        if form.is_valid():
            ulasan = form.save(commit=False)
            ulasan.userid = request.user
            ulasan.bukuid = buku
            ulasan.save()
            return redirect('ulasanbuku:list')  # Ganti 'daftar_buku' dengan URL yang sesuai untuk menampilkan daftar buku
    else:
        form = UlasanBukuForm()
    return render(request, 'ulasan/ulasan_form.html', {'form': form, 'buku': buku})

@login_required
def view_ulasan(request, bukuid):
    buku = get_object_or_404(Buku, pk=bukuid)
    ulasan = Ulasanbuku.objects.filter(bukuid=buku)  # Mengambil ulasan yang sesuai dengan buku yang diinginkan
    return render(request, 'ulasan/lihat_ulasan.html', {'buku': buku, 'ulasan': ulasan})

@login_required
def ulasan_list(request):
    ulasan = Ulasanbuku.objects.filter(userid=request.user)
    return render(request, 'ulasan/daftar_ulasan.html', {'ulasan': ulasan})

@login_required
def update_ulasan(request, ulasanid):
    ulasan = get_object_or_404(Ulasanbuku, pk=ulasanid)
    if request.method == 'POST':
        form = UlasanBukuForm(request.POST, instance=ulasan)
        if form.is_valid():
            form.save()
            return redirect('ulasanbuku:list')
    else:
        form = UlasanBukuForm(instance=ulasan)
    return render(request, 'ulasan/ulasan_form.html', {'form': form})

@login_required
def delete_ulasan(request, ulasanid):
    ulasan = get_object_or_404(Ulasanbuku, pk=ulasanid)
    if request.method == 'POST':
        ulasan.delete()
        return redirect('ulasanbuku:list')
    return redirect('ulasanbuku:list')
