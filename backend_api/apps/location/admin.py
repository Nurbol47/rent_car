from django.contrib import admin
from django.utils.text import Truncator
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

    def description(self, obj):
        return Truncator(obj.description).chars(100)
    description.short_description = 'Описание'


@admin.register(Characteristic)
class CharacteristicAdmin(admin.ModelAdmin):
    list_display = ['location', 'title', 'parameter']


@admin.register(ImgLocation)
class ImgLocationAdmin(admin.ModelAdmin):
    list_display = ['location', 'img']