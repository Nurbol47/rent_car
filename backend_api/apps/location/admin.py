from django.contrib import admin
from django import forms
from .inlines import *
from .models import *


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ['title', 'img', 'description']
    inlines = [CharacteristicInline]
    filter_horizontal = ['cars']


@admin.register(Characteristic)
class CharacteristicAdmin(admin.ModelAdmin):
    list_display = ['location', 'title', 'parameter']