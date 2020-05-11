from django.urls import path

# untuk mengambil views
from . import views

urlpatterns = [
    path('', views.index),

    # untuk menampilkan  data
    path('lihat/', views.lihat, name='lihat'),

    # untuk menampilkan form tambah
    path('lihat/add', views.add, name='add'),
    path('lihat/add/add_post', views.add_post, name='add_post'),

    # untuk menapilkan form ubah
    path('lihat/upd/<int:id>', views.upd, name='upd'),
    path('lihat/upd/upd_post', views.upd_post, name='upd_post'),

    # untuk menghapus data
    path('lihat/del/<int:id>', views.trush, name='trush'),

    # untuk menampilkan detail
    path('detail/<int:id>', views.detail, name='detail'),
]
