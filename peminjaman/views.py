from django.shortcuts import render, redirect, get_object_or_404
from .models import Peminjaman
from buku.models import Buku
from .forms import PeminjamanForm
from django.forms import HiddenInput
from django.http import HttpResponse
from xhtml2pdf import pisa
from django.contrib import messages
from django.template.loader import get_template
from django.contrib.auth.decorators import login_required

# Fitur Peminjaman
@login_required
def Peminjaman_list(request):
    pinjams = Peminjaman.objects.filter(userid=request.user)
    return render(request, 'peminjaman/daftar_peminjaman.html', {'pinjams': pinjams})

def create_Peminjaman(request, bukuid):
    buku = get_object_or_404(Buku, pk=bukuid)  # Ambil objek buku berdasarkan ID yang diberikan
    if request.method == 'POST':
        form = PeminjamanForm(request.POST)
        if form.is_valid():
            print("Form is valid!")
            peminjaman = form.save(commit=False)
            peminjaman.userid = request.user  # Set nilai User ID dengan pengguna yang sedang login
            peminjaman.bukuid = buku  # Set nilai Book ID dengan objek buku yang diberikan
            peminjaman.save()
            return redirect('Peminjaman:read')
        else:
            # Tambahkan pesan kesalahan jika validasi gagal
            messages.error(request, 'Terdapat kesalahan dalam pengisian formulir.')
    else:
        form = PeminjamanForm(initial={'userid': request.user, 'bukuid': buku.pk})
        
    return render(request, 'peminjaman/peminjaman_form.html', {'form': form, 'buku': buku})

# Menampilkan total data
def total_peminjaman_per_user(request):
    if request.user.is_authenticated:
        total = Peminjaman.objects.filter(userid=request.user).count()
        return total
    else:
        return 0

# Fitur Admin
def admin_peminjaman_list(request):
    pinjams = Peminjaman.objects.all()
    return render(request, 'peminjaman/admin_daftar_peminjaman.html', {'pinjams': pinjams})

def update_Peminjaman(request, peminjamanid):
    peminjaman = get_object_or_404(Peminjaman, peminjamanid=peminjamanid)
    if request.method == 'POST':
        form = PeminjamanForm(request.POST, instance=peminjaman)
        if form.is_valid():
            form.save()
            return redirect('Peminjaman:admin-read')
    else:
        form = PeminjamanForm(instance=peminjaman)
        # Periksa apakah bidang 'peminjamanid' ada dalam form
        if 'peminjamanid' in form.fields:
            form.fields['peminjamanid'].widget = HiddenInput()

    return render(request, 'peminjaman/admin_peminjaman_form.html', {'form': form})

def delete_Peminjaman(request, peminjamanid):
    peminjaman = get_object_or_404(Peminjaman, peminjamanid=peminjamanid)
    peminjaman.delete()
    return redirect('Peminjaman:admin-read')

def generate_laporan_peminjaman(request, peminjaman_id):
    peminjaman = get_object_or_404(Peminjaman, peminjamanid=peminjaman_id)
    template_path = 'peminjaman/generate_laporan_peminjaman.html'
    context = {'peminjaman': peminjaman}
    # Render template
    template = get_template(template_path)
    html = template.render(context)
    # Create PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="laporan_peminjaman_{}.pdf"'.format(peminjaman.peminjamanid)
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

# Menampilkan total data admin dan petugas
def total_data_peminjaman():
    total = Peminjaman.objects.all().count()
    return total  # Mengembalikan total tanpa menggunakan dictionary

# Fitur petugas
def petugas_peminjaman_list(request):
    pinjams = Peminjaman.objects.all()
    return render(request, 'peminjaman/petugas_daftar_peminjaman.html', {'pinjams': pinjams})

def update_Peminjaman_petugas(request, peminjamanid):
    peminjaman = get_object_or_404(Peminjaman, peminjamanid=peminjamanid)
    if request.method == 'POST':
        form = PeminjamanForm(request.POST, instance=peminjaman)
        if form.is_valid():
            form.save()
            return redirect('Peminjaman:petugas-read')
    else:
        form = PeminjamanForm(instance=peminjaman)
        # Periksa apakah bidang 'peminjamanid' ada dalam form
        if 'peminjamanid' in form.fields:
            form.fields['peminjamanid'].widget = HiddenInput()

    return render(request, 'peminjaman/petugas_peminjaman_form.html', {'form': form})

def delete_Peminjaman_petugas(request, peminjamanid):
    peminjaman = get_object_or_404(Peminjaman, peminjamanid=peminjamanid)
    peminjaman.delete()
    return redirect('Peminjaman:petugas-read')