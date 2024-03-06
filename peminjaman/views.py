from django.shortcuts import render, redirect, get_object_or_404
from .models import Peminjaman
from buku.models import Buku
from .forms import PeminjamanForm
from django.forms import HiddenInput
from django.http import HttpResponse
from xhtml2pdf import pisa
from django.template.loader import get_template

def admin_peminjaman_list(request):
    pinjams = Peminjaman.objects.all()
    return render(request, 'peminjaman/admin_daftar_peminjaman.html', {'pinjams': pinjams})

def Peminjaman_list(request):
    pinjams = Peminjaman.objects.all()
    return render(request, 'peminjaman/daftar_peminjaman.html', {'pinjams': pinjams})

def create_Peminjaman(request,bukuid):
    if request.method == 'POST':
        form = PeminjamanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Peminjaman:read')
    else:
        form = PeminjamanForm()
        
    buku = Buku.objects.get(pk=bukuid)
    return render(request, 'peminjaman/peminjaman_form.html', {'form': form})

def update_Peminjaman(request, peminjamanid):
    peminjaman = get_object_or_404(Peminjaman, peminjamanid=peminjamanid)
    if request.method == 'POST':
        form = PeminjamanForm(request.POST, instance=peminjaman)
        if form.is_valid():
            form.save()
            return redirect('Peminjaman:read')
    else:
        form = PeminjamanForm(instance=peminjaman)
        form.fields['peminjamanid'].widget = HiddenInput()

    return render(request, 'peminjaman/admin_peminjaman_form.html', {'form': form})

def delete_Peminjaman(request, peminjamanid):
    peminjaman = get_object_or_404(Peminjaman, peminjamanid=peminjamanid)
    peminjaman.delete()
    return redirect('Peminjaman:read')

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