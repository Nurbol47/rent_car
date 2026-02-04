from django.db import models
from django.db.models import Sum
from django.core.exceptions import ValidationError
from apps.price.models import *

class Car(models.Model):
    FUEL_CHOICES = [
        ('petrol', 'Бензин'),
        ('diesel', 'Дизель'),
        ('gas', 'Газ'),
        ('electric', 'Электрический'),
        ('hybrid', 'Гибрид'),
    ]

    name = models.CharField("Название", max_length=150, blank=True)
    img = models.ImageField("Изображение", upload_to='img_car/')
    brand = models.CharField("Марка", max_length=150)
    model = models.CharField("Модель", max_length=150)
    seating = models.PositiveIntegerField("Посадочные места", default=0)
    engine_power = models.FloatField("Мощность двигателя")
    fuel_type = models.CharField("Вид топлива", choices=FUEL_CHOICES, default='petrol')
    body_car = models.CharField("Кузов", max_length=150)
    year_of_manufacture = models.PositiveIntegerField("Год выпуска")
    duration_start = models.DateField("Дата начало")
    duration_end = models.DateField("Дата конец")
    discount = models.PositiveIntegerField("Скидка (%)", default=0)
    pledge = models.DecimalField("Залог", decimal_places=2, max_digits=10, default=0)

    @property
    def rental_days(self):
        delta = self.duration_end - self.duration_start
        days = delta.days
        return days if days > 0 else 1

    @property
    def total_price(self):
        # 1. Ищем активный план, подходящий под текущие даты/длительность
        activate_plan = self.plans.filter(is_active=True).first()
        
        if not activate_plan:
            return 0

        # 2. Считаем сумму доп. услуг через агрегацию
        services_sum = activate_plan.extra_service.aggregate(total=Sum('price'))['total'] or 0
        
        # 3. Базовая стоимость (цена плана * дни)
        base_cost = activate_plan.price_period * self.rental_days
        
        return base_cost + services_sum
    
    @property
    def price_with_discount(self):
        total = self.total_price
        if self.discount > 0:
            return total - (total * self.discount / 100)
        return total
    
    def save(self, *args, **kwargs):
        # Автоматическое формирование имени перед сохранением
        self.name = f"{self.brand} {self.model}".strip()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Машина"
        verbose_name_plural = "Машины"


class CarWashOption(models.Model):
    price_wash = models.DecimalField("Цена мойки", max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.price_wash}"
    
    class Meta:
        verbose_name = "Цена на мойку"
        verbose_name_plural = "Цены на мойку"


class BookCar(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name="bookings", verbose_name="Машина")
    child_seat = models.BooleanField("Детское кресло", default=False)
    has_wash_type = models.ForeignKey(CarWashOption, on_delete=models.SET_NULL, null=True, verbose_name='Тип мойки')
    is_wish = models.BooleanField("Нужна мойка", default=True)
    car_delivery = models.BooleanField("Подача авто", default=False)
    call_time = models.DateTimeField("Время создания заявки", auto_now_add=True)
    is_city = models.BooleanField("По городу", default=True)
    is_airport = models.BooleanField("В аэропорт", default=False)

    def __str__(self):
        return f"Бронь: {self.car.name} ({self.call_time.strftime('%d.%m.%Y')})"
    
    class Meta:
        verbose_name = "Бронирование"
        verbose_name_plural = "Бронирования"

