from django.shortcuts import render

from . forms import Tamu

def index(request):
    buku_tamu = Tamu()

    context = {
        'BukuTamu' : buku_tamu,
    }

    return render(request, 'tamu/index.html', context)