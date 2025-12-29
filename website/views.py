from django.shortcuts import render, get_object_or_404
from .models import Berita, Dosen

def index(request):
    berita_list = Berita.objects.all().order_by('-tanggal')[:3]
    dosen_list = Dosen.objects.all()
    
    context = {
        'berita': berita_list,
        'dosen': dosen_list,
    }
    return render(request, 'index.html', context)

def detail_berita(request, id):
    berita = get_object_or_404(Berita, id=id)
    return render(request, 'detail_berita.html', {'berita': berita})