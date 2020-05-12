from django.urls import path

# untuk mengambil views
from . import views

urlpatterns = [
    path('', views.index),
    # untuk login
    path('login/', views.login, name='login'),
    path('login/check_validation/', views.check_validation, name='check_validation'),
    # untuk logout
    path('logout/', views.logout, name='logout'),
]
