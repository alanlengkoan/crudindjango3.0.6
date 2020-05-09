from django.contrib import admin

# Register your models here.

# untuk mengambil model single
from .models import Tampil
# untuk mengambil semua models
from . import models

admin.site.register(Tampil)
