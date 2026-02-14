from django.contrib import admin
from .models import Car, CarWashOption, BookCar, UserModel, ImgCar
from .inlines import ImgCarInline


@admin.register(ImgCar)
class ImgCarAdmin(admin.ModelAdmin):
    list_display = ['id', 'img', 'car']
    list_filter = ['car']


@admin.register(CarWashOption)
class CarWashOptionAdmin(admin.ModelAdmin):
    list_display = ['id', 'price_wash']
    list_editable = ['price_wash'] 


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['name', 'brand', 'model', 'color', 'drive_unit', 'body_car', 'year_of_manufacture', 'discount']
    list_filter = ['brand', 'fuel_type', 'body_car'] 
    search_fields = ['name', 'brand', 'model']
    inlines = [ImgCarInline]
    

@admin.register(BookCar)
class BookCarAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'user', 'car', 'duration_start', 
        'duration_end', 'rental_days', 'total_price_snapshot', 'status'
    ]
    
    list_filter = ['duration_start', 'car', 'user', 'status']
    
    search_fields = ['user__username', 'car__name']
    
    readonly_fields = ['total_price_snapshot', 'call_time']
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('user', 'car', 'call_time', 'status')
        }),
        ('Даты аренды', {
            'fields': ('duration_start', 'duration_end')
        }),
        ('Дополнительные услуги', {
            'fields': ('child_seat', 'is_wish', 'has_wash_type', 'car_delivery')
        }),
        ('Локация', {
            'fields': ('is_city', 'is_airport')
        }),
        ('Финансы', {
            'fields': ('total_price_snapshot',),
            'description': 'Цена рассчитывается автоматически при сохранении'
        }),
    )


@admin.register(UserModel)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone', 'agreement')
    
    list_display_links = ('full_name',)
    
    list_filter = ('agreement',)
