from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
from django.db.models import Sum, Q


class ImgCar(models.Model):
    img = models.ImageField("Изображение", upload_to='img_car/')
    car = models.ForeignKey('Car', on_delete=models.CASCADE, related_name='img', verbose_name="Машина")

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"

    def __str__(self):
        return str(self.img.name)


class Car(models.Model):
    """
    Модель транспортного средства.
    Хранит технические характеристики и параметры ценообразования (скидки, залог).
    """
    FUEL_CHOICES = [
        ('petrol', 'Бензин'),
        ('diesel', 'Дизель'),
        ('gas', 'Газ'),
        ('electric', 'Электрический'),
        ('hybrid', 'Гибрид'),
    ]

    name = models.CharField("Название", max_length=150, blank=True)
    brand = models.CharField("Марка", max_length=150)
    model = models.CharField("Модель", max_length=150)
    seating = models.PositiveIntegerField("Посадочные места", default=0)
    engine_power = models.FloatField("Мощность двигателя")

    color = models.CharField("Цвет", max_length=50, blank=True)
    drive_unit = models.CharField("Привод", max_length=50, blank=True) # Например: AWD, RWD, FWD
   
    fuel_type = models.CharField("Вид топлива", choices=FUEL_CHOICES, default='petrol')
    body_car = models.CharField("Кузов", max_length=150)
    duration_start = models.DateField("Дата начала")
    duration_end = models.DateField("Дата конца")
    year_of_manufacture = models.PositiveIntegerField("Год выпуска")
    discount = models.PositiveIntegerField("Скидка (%)", default=0)
    pledge = models.DecimalField("Залог", decimal_places=2, max_digits=10, default=0)

    def get_current_price(self):
        """Возвращает базовую цену из активного плана"""
        active_plan = self.plans.filter(is_active=True).first()
        return active_plan.price_period if active_plan else 0

    def get_discounted_price(self):
        """Возвращает цену с учетом скидки"""
        price = self.get_current_price()
        if self.discount > 0:
            return int(float(price) * (1 - self.discount / 100))
        return price

    def save(self, *args, **kwargs):
        # Автоматическое формирование полного названия при сохранении
        self.name = f"{self.brand} {self.model}".strip()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Машина"
        verbose_name_plural = "Машины"


class CarWashOption(models.Model):
    """Справочник типов мойки и их стоимости"""
    price_wash = models.DecimalField("Цена мойки", max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.price_wash}"
    
    class Meta:
        verbose_name = "Тип мойки"
        verbose_name_plural = "Типы мойки"


class BookCar(models.Model):
    """
    Модель бронирования автомобиля.
    Включает расчет стоимости, валидацию дат и фиксацию итоговой цены (snapshot).
    """
    STATUS_CHOICES = [
        ('pending', 'Ожидание'),
        ('confirmed', 'Подтверждено'),
        ('cancelled', 'Отменено'),
        ('completed', 'Завершено'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Пользователь")
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name="bookings", verbose_name="Машина")
    
    duration_start = models.DateField("Дата начала")
    duration_end = models.DateField("Дата конца")
 
    status = models.CharField("Статус", max_length=20, choices=STATUS_CHOICES, default='pending')
    
    # Фиксируем цену на момент бронирования, чтобы изменения в тарифах не влияли на старые заказы
    total_price_snapshot = models.DecimalField("Итоговая цена", max_digits=12, decimal_places=2, editable=False, default=0)
    
    child_seat = models.BooleanField("Детское кресло", default=False)
    has_wash_type = models.ForeignKey(CarWashOption, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Тип мойки')
    is_wish = models.BooleanField("Нужна мойка", default=True)
    car_delivery = models.BooleanField("Подача авто", default=False)
    call_time = models.DateTimeField("Время создания заявки", auto_now_add=True)
    is_city = models.BooleanField("По городу", default=True, null=True, blank=True)
    is_airport = models.BooleanField("В аэропорт", default=False, null=True, blank=True)

    @property
    def rental_days(self):
        """Возвращает количество полных дней аренды (минимум 1)"""
        delta = self.duration_end - self.duration_start
        return max(delta.days, 1)

    def calculate_total_price(self):
        """
        Рассчитывает стоимость аренды на основе активного плана, 
        длительности, доп. услуг и мойки с учетом скидки автомобиля.
        """
        active_plan = self.car.plans.filter(is_active=True).first()
        
        if not active_plan:
            return 0
        
        base_cost = active_plan.price_period * self.rental_days
        services_sum = active_plan.extra_service.aggregate(total=Sum('price'))['total'] or 0
        wash_cost = self.has_wash_type.price_wash if (self.is_wish and self.has_wash_type) else 0
        
        total = base_cost + services_sum + wash_cost
        
        # Применяем процентную скидку, если она указана в модели Car
        if self.car.discount > 0:
            total -= (total * self.car.discount / 100)
            
        return total

    def clean(self):
        """Валидация бизнес-логики перед сохранением в БД"""
        if self.duration_start and self.duration_end:
            # 1. Проверка корректности периода
            if self.duration_start >= self.duration_end:
                raise ValidationError("Дата окончания должна быть позже даты начала.")

            # 2. Проверка на пересечение дат с существующими активными бронированиями
            overlap = BookCar.objects.filter(
                car=self.car,
                status__in=['pending', 'confirmed'],
                duration_start__lt=self.duration_end,
                duration_end__gt=self.duration_start
            ).exclude(pk=self.pk)

            if overlap.exists():
                raise ValidationError(f"Машина {self.car.name} уже забронирована на этот период.")

    def save(self, *args, **kwargs):
        # Принудительный запуск чистки данных (валидации)
        self.full_clean()
        # Фиксация итоговой цены перед записью в базу
        self.total_price_snapshot = self.calculate_total_price()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Бронирование #{self.id}: {self.car.name} ({self.status})"
    
    class Meta:
        verbose_name = "Бронирование"
        verbose_name_plural = "Бронирования"


class UserModel(models.Model):
    booking = models.OneToOneField(BookCar, on_delete=models.CASCADE, related_name="contact_info", verbose_name="Бронирование")

    full_name = models.CharField("ФИО", max_length=150)
    phone = models.CharField("Телефон", max_length=20)

    agreement = models.BooleanField("Согласие на обработку персональных данных", default=False)

    class Meta:
        verbose_name = "Данные клиента"
        verbose_name_plural = "Данные клиентов"

    def __str__(self):
        return f"{self.full_name} ({self.phone})"