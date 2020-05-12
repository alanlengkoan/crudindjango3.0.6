# untuk response
from django.http import HttpResponse
# untuk mengrender .html
from django.shortcuts import render
# untuk redirect
from django.shortcuts import redirect
# untuk conection
from django.db import connection
# untuk mengambil semua models
from . import models

# variabel global
cursor = connection.cursor()

# untuk halaman index
def index(request):
    if request.session.keys():
        return HttpResponse('halaman admin')
    else:
        return redirect('/admin/login/')

# begin:: auth
def login(request):
    return render(request, 'login.html')

# untuk check data user
def check_validation(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        result = models.Users.objects.filter(username=username, password=password).count()
        if result != 0:

            request.session['username'] = username
            request.session['login'] = 'true'
            
            return redirect('/admin/')
        else:
            return redirect('/admin/login/')


    return HttpResponse('halaman check')

# untuk logout
def logout(request):
    del request.session['username']
    del request.session['login']

    return redirect('/admin/login/')
# end:: auth
