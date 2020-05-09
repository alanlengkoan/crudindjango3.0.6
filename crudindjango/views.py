# untuk response
from django.http import HttpResponse
# untuk mengrender .html
from django.shortcuts import render


def index(request):
    # return HttpResponse('halo alan')
    data = {
        'title': 'Home',
        'halaman': 'Halo Alan!',
        'menu': [
            ['/tentang', 'Tentang'],
            ['/kontak', 'Kontak'],
            ['/show', 'Show'],
        ],
    }
    return render(request, 'index.html', data)


def tentang(request):
    # return HttpResponse('halaman tentang')
    data = {
        'title': 'About',
        'halaman': 'Tentang',
        'menu': [
            ['/tentang', 'Tentang'],
            ['/kontak', 'Kontak'],
            ['/show', 'Show'],
        ],
    }
    return render(request, 'index.html', data)


def kontak(request):
    # return HttpResponse('halaman kontak')
    data = {
        'title': 'Contact',
        'halaman': 'Kontak',
        'menu': [
            ['/tentang', 'Tentang'],
            ['/kontak', 'Kontak'],
            ['/show', 'Show'],
        ],
    }
    return render(request, 'index.html', data)
