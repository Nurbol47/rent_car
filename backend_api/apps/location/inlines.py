from django.contrib import admin
from .models import *

class CharacteristicInline(admin.TabularInline):
    model = Characteristic
    extra = 1


class ImgLocationInline(admin.TabularInline):
    model = ImgLocation
    extra = 1