from django.contrib import admin
from django import forms
from .inlines import *
from .models import *


@admin.register(BaseLocation)
class BaseLocationAdmin(admin.ModelAdmin):
    list_display = ['title', 'img']


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']
    inlines = [CharacteristicInline, ImgLocationInline]
    filter_horizontal = ['cars']


@admin.register(Characteristic)
class CharacteristicAdmin(admin.ModelAdmin):
    list_display = ['location', 'title', 'parameter']


@admin.register(ImgLocation)
class ImgLocationAdmin(admin.ModelAdmin):
    list_display = ['location', 'img']