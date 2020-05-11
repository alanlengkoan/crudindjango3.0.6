# untuk response
from django.http import HttpResponse
# untuk mengrender .html
from django.shortcuts import render
# untuk redirect
from django.shortcuts import redirect
# untuk mengambil semua models
from . import models

# untuk halaman index
def index(request):
    # untuk mengambil data dari database
    result = models.Tampil.objects.all()

    data = {
        'title': 'Show',
        'halaman': 'Show',
        'menu': [
            ['/tentang', 'Tentang'],
            ['/kontak', 'Kontak'],
            ['/show', 'Show'],
            ['/show/lihat', 'Lihat']
        ],
        'result': result
    }
    return render(request, 'show/index.html', data)

# untuk halaman detail
def detail(request, id):    
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

# untuk halaman lihat data
def lihat(request):
    # untuk mengambil semua data
    result = models.Tampil.objects.all()

    data = {
        'title': 'Lihat data',
        'halaman': 'Lihat data',
        'menu': [
            ['/tentang', 'Tentang'],
            ['/kontak', 'Kontak'],
            ['/show', 'Show'],
            ['/show/lihat', 'Lihat']
        ],
        'result': result
    }
    return render(request, 'show/lihat.html', data)

# untuk tambah data
def add(request):
    data = {
        'title': 'Tambah data',
        'halaman': 'Tambah data',
        'menu': [
            ['/tentang', 'Tentang'],
            ['/kontak', 'Kontak'],
            ['/show', 'Show'],
            ['/show/lihat', 'Lihat']
        ],
    }

    return render(request, 'show/add.html', data)

# untuk proses tambah
def add_post(request):

    if request.method == 'POST':
        tampil = models.Tampil()
        tampil.title = request.POST['inp_judul']
        tampil.body = request.POST['inp_isi']
        tampil.save()
    
    return redirect('/show/lihat/')

# untuk ubah data
def upd(request, id):
    # untuk mengambil data dari database
    result = models.Tampil.objects.get(pk=id)

    data = {
        'title': 'Tambah data',
        'halaman': 'Tambah data',
        'menu': [
            ['/tentang', 'Tentang'],
            ['/kontak', 'Kontak'],
            ['/show', 'Show'],
            ['/show/lihat', 'Lihat']
        ],
        'result': result
    }

    return render(request, 'show/upd.html', data)

# untuk proses update
def upd_post(request):

    if request.method == 'POST':
        id = request.POST['inp_id']
        
        tampil = models.Tampil.objects.get(id=id)
        tampil.title = request.POST['inp_judul']
        tampil.body = request.POST['inp_isi']
        tampil.save()
    
    return redirect('/show/lihat/')

# untuk proses hapus
def trush(request, id):
    models.Tampil.objects.get(id=id).delete()
    
    return redirect('/show/lihat/')

# def tampil(request):
#     # return HttpResponse('halaman tentang')
#     return HttpResponse('halaman tampil')
