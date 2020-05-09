# untuk response
from django.http import HttpResponse
# untuk mengrender .html
from django.shortcuts import render
# untuk mengambil semua models
from . import models

# untuk halaman index
def index(request):
    # return HttpResponse('halaman tentang')

    # untuk mengambil data dari database
    result = models.Tampil.objects.all()

    data = {
        'title': 'Show',
        'halaman': 'Show',
        'menu': [
            ['/tentang', 'Tentang'],
            ['/kontak', 'Kontak'],
            ['/show', 'Show'],
            ['/show/tampil', 'Tampil']
        ],
        'result': result
    }
    return render(request, 'show/index.html', data)

def detail(request, id):
    # return HttpResponse('halaman tentang')
    
    # untuk mengambil data dari database
    result = models.Tampil.objects.get(pk=id)
    
    data = {
        'title': 'Detail show',
        'menu': [
            ['/tentang', 'Tentang'],
            ['/kontak', 'Kontak'],
            ['/show', 'Show'],
        ],
        'result': result
    }

    return render(request, 'show/detail.html', data)

def tampil(request):
    # return HttpResponse('halaman tentang')
    return HttpResponse('halaman tampil')


