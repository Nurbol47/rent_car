from django.db import models


class Car(models.Model):
    name = models.CharField("Машина", max_length=150)

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
    name = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name="Название")
    duration_start = models.DateField("Дата начало", auto_now=True)
    duration_end = models.DateField("Дата конец", auto_now=True)
    child_seat = models.BooleanField("Детское кресло", default=True)
    has_wish_type = models.ForeignKey(CarWashOption, on_delete=models.CASCADE, verbose_name='Цена мойки')
    is_wish = models.BooleanField("Мойка", default=True)
    car_delivery = models.BooleanField("Подача авто", default=True)
    call_time = models.TimeField("Время вызова", auto_now=True)
    is_city = models.BooleanField("Город", default=False)
    is_airport = models.BooleanField("Аэропорт", default=True)
    total_price = models.DecimalField("Общая цена", decimal_places=2, max_digits=10)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Бронирование машины"
        verbose_name_plural = "Бронирование машин"
