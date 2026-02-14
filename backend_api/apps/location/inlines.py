from django.contrib import admin
from .models import *

class CharacteristicInline(admin.TabularInline):
    model = Characteristic
    extra = 2


class ImgLocationInline(admin.TabularInline):
    model = ImgLocation
    extra = 3