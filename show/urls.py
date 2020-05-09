from django.urls import path

# untuk mengambil views
from . import views

urlpatterns = [
    path('', views.index),
    path('tampil/', views.tampil, name='tampil'),
    path('detail/<int:id>', views.detail, name='detail'),
]
