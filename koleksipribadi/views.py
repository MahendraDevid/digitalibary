from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Koleksipribadi
from .forms import KoleksipribadiForm
from buku.models import Buku

@login_required
def koleksipribadi_list(request):
    koleksi = Koleksipribadi.objects.filter(userid=request.user.userid)
    return render(request, 'koleksipribadi/koleksipribadi_list.html', {'koleksi': koleksi})

@login_required
def create_koleksipribadi(request, bukuid):
    buku = get_object_or_404(Buku, pk=bukuid)
    if request.method == 'POST':
        form = KoleksipribadiForm(request.POST)
        if form.is_valid():
            koleksi = form.save(commit=False)
            koleksi.userid = request.user
            if buku is not None:
                koleksi.bukuid = buku
                koleksi.save()
                return redirect('koleksipribadi:list')
            else:
                # Handle invalid bukuid here
                return HttpResponse("Invalid Buku ID")
    else:
        form = KoleksipribadiForm()
    return render(request, 'koleksipribadi/create_koleksipribadi.html', {'form': form, 'buku': buku})

@login_required
def delete_koleksipribadi(request, koleksi_id):
    koleksi = get_object_or_404(Koleksipribadi, koleksiid=koleksi_id)
    if request.method == 'POST':
        koleksi.delete()
        return redirect('koleksipribadi:list')
    return redirect('koleksipribadi:list')

