from django.db import models
from django.core.exceptions import ValidationError
from apps.car.models import Car

class MonthChoices(models.IntegerChoices):
    """Перечисление месяцев для строгой типизации сезонов"""
    JANUARY = 1, 'Январь'
    FEBRUARY = 2, 'Февраль'
    MARCH = 3, 'Март'
    APRIL = 4, 'Апрель'
    MAY = 5, 'Май'
    JUNE = 6, 'Июнь'
    JULY = 7, 'Июль'
    AUGUST = 8, 'Август'
    SEPTEMBER = 9, 'Сентябрь'
    OCTOBER = 10, 'Октябрь'
    NOVEMBER = 11, 'Ноябрь'
    DECEMBER = 12, 'Декабрь'


class Season(models.Model):
    """
    Модель временных интервалов (сезонов). 
    Используется для автоматического изменения цен в зависимости от времени года.
    """
    month_from = models.PositiveSmallIntegerField("С (месяц)", choices=MonthChoices.choices, default=1)
    month_to = models.PositiveSmallIntegerField("По (месяц)", choices=MonthChoices.choices, default=1)

    def __str__(self):
        return f"{self.get_month_from_display()} — {self.get_month_to_display()}"
    
    class Meta:
        verbose_name = "Сезон"
        verbose_name_plural = "Сезоны"


class ExtraService(models.Model):
    """
    Дополнительные услуги (детское кресло, GPS, полная страховка).
    Поддерживает расчет как за услугу целиком, так и посуточно.
    """
    title = models.CharField("Название", max_length=150)
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    max_price = models.DecimalField("Лимит цены", max_digits=10, decimal_places=2, null=True, blank=True)
    
    # Временные ограничения для услуг (например, аренда только в рабочее время)
    start_time = models.TimeField("Время начала", null=True, blank=True)
    end_time = models.TimeField("Время окончания", null=True, blank=True)
    
    is_per_day = models.BooleanField("Расчет посуточно", default=False)

    def __str__(self):
        return self.title
    
    def clean(self):
        """Бизнес-валидация стоимостных рамок"""
        if self.max_price and self.max_price < self.price:
            raise ValidationError({'max_price': "Максимальный лимит не может быть меньше базовой цены."})
    
    class Meta:
        verbose_name = "Доп. услуга"
        verbose_name_plural = "Доп. услуги"


class PricingPlan(models.Model):
    """
    Сложная модель ценообразования. 
    Связывает машину, сезон и длительность аренды для определения стоимости.
    """
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name="plans", verbose_name="Машина")
    season = models.ForeignKey(Season, on_delete=models.CASCADE, related_name="plans", verbose_name="Сезон")
    
    min_day = models.PositiveIntegerField("Дней от")
    max_day = models.PositiveIntegerField("Дней до", null=True, blank=True)
    
    price_period = models.DecimalField("Стоимость (в сутки)", decimal_places=2, max_digits=15)
    extra_service = models.ManyToManyField(ExtraService, blank=True, verbose_name="Включенные услуги")
    
    is_active = models.BooleanField("План активен", default=True)

    def __str__(self):
        return f"{self.car.name} | {self.season} | {self.price_period} руб/день"
    
    def clean(self):
        """Проверка логической последовательности дней аренды"""
        if self.max_day and self.max_day <= self.min_day:
            raise ValidationError({'max_day': "Верхний порог дней должен превышать минимальный."})
    
    class Meta:
        verbose_name = "Тарифный план"
        verbose_name_plural = "Тарифные планы"
        # Сортировка по минимальному количеству дней для удобства отображения
        ordering = ['car', 'min_day']