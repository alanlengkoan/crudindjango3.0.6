from django.contrib import admin
from django.urls import path,  include

# untuk mengambil views
from . import views
# from show import views as show

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('tentang/', views.tentang, name='tentang'),
    path('kontak/', views.kontak, name='kontak'),

    # path('show/', show.index)
    path('show/', include('show.urls')),
]
