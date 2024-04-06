from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Koleksipribadi
from .forms import KoleksipribadiForm
from buku.models import Buku

# Fitur Peminjam
@login_required
def koleksipribadi_list(request):
    koleksi = Koleksipribadi.objects.filter(userid=request.user)
    return render(request, 'koleksipribadi/koleksipribadi_list.html', {'koleksi': koleksi})

@login_required
def create_koleksipribadi(request, bukuid):
    # Ambil objek buku berdasarkan ID yang diberikan
    buku = get_object_or_404(Buku, pk=bukuid)
    if request.method == 'POST':
        form = KoleksipribadiForm(request.POST)
        if form.is_valid():
            koleksi = form.save(commit=False)
            # Set nilai User ID dengan pengguna yang sedang login
            koleksi.userid = request.user
            # Set nilai Book ID dengan objek buku yang diberikan
            koleksi.bukuid = buku
            koleksi.save()
            return redirect('koleksipribadi:list')
    else:
        # Inisialisasi form dengan nilai-nilai awal
        form = KoleksipribadiForm()
    return render(request, 'koleksipribadi/create_koleksipribadi.html', {'form': form, 'buku': buku})

# Meenampilkan Total data
def total_koleksi_per_user(request):
    if request.user.is_authenticated:
        total = Koleksipribadi.objects.filter(userid=request.user).count()
        return total
    else:
        return 0

@login_required
def delete_koleksipribadi_peminjam(request, koleksi_id):
    koleksi = get_object_or_404(Koleksipribadi, pk=koleksi_id)
    koleksi.delete()
    return redirect('koleksipribadi:list')

# Fitur Admin
def koleksipribadi_admin_list(request):
    koleksi = Koleksipribadi.objects.all()
    return render(request, 'koleksipribadi/koleksipribadi_admin_list.html', {'koleksi': koleksi})

@login_required
def delete_koleksipribadi(request, koleksi_id):
    koleksi = get_object_or_404(Koleksipribadi, pk=koleksi_id)
    koleksi.delete()
    return redirect('koleksipribadi:list-admin')

# Menampilkan untuk admin
def total_data_koleksi():
    total = Koleksipribadi.objects.all().count()
    return total

