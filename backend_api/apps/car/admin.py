from django.contrib import admin
from .models import *

@admin.register(CarWashOption)
class CarWishOptionAdmin(admin.ModelAdmin):
    list_display = ['price_wash']


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_dispaly = ['name']

# @admin.register(BookCar)
# class BookCarAdmin(admin.ModelAdmin):
#     list_display = ['']
