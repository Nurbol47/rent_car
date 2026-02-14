from django.contrib import admin
from .models import *

class ImgCarInline(admin.TabularInline):
    model = ImgCar
    extra = 3
    