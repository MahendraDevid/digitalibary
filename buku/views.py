from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Buku
from .forms import BukuForm

def daftar_buku(request):
    bukus = Buku.objects.all()
    return render(request, 'buku/daftar_buku.html', {'bukus': bukus})

def peminjam_daftar_buku(request):
    bukus = Buku.objects.all()
    return render(request, 'buku/peminjam_daftar_buku.html', {'bukus': bukus})

def tambah_buku(request):
    if request.method == 'POST':
        form = BukuForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('daftar_buku')
    else:
        form = BukuForm()
    return render(request, 'buku/buku_form.html', {'form': form})

def ubah_buku(request, buku_id):
    buku = get_object_or_404(Buku, pk=buku_id)
    if request.method == 'POST':
        form = BukuForm(request.POST, instance=buku)
        if form.is_valid():
            form.save()
            return redirect('daftar_buku')
    else:
        form = BukuForm(instance=buku)
    return render(request, 'buku/buku_form.html', {'form': form})

def hapus_buku(request, buku_id):
    buku = get_object_or_404(Buku, pk=buku_id)
    if request.method == 'POST':
        buku.delete()
        return redirect('daftar_buku')  # Arahkan pengguna kembali ke daftar buku setelah menghapus buku
    else:
        # Tidak perlu menampilkan konfirmasi di halaman template, langsung lakukan penghapusan dan arahkan kembali ke daftar buku
        buku.delete()
        return redirect('daftar_buku')

