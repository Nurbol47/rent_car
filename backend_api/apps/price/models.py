from django.db import models
from django.core.exceptions import ValidationError
from apps.car.models import Car


class MonthChoices(models.IntegerChoices):
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
    month_from = models.PositiveSmallIntegerField("От (месяцa)", choices=MonthChoices, default=1)
    month_to = models.PositiveSmallIntegerField("До (месяцa)", choices=MonthChoices, default=1)

    def __str__(self):
        return f"{self.get_month_from_display()} - {self.get_month_to_display()}"
    
    class Meta:
        verbose_name = "Сезон"
        verbose_name_plural = "Сезоны"


class ExtraService(models.Model):
    title = models.CharField("Название", max_length=150)
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    max_price = models.DecimalField("Максимальная цена", max_digits=10, decimal_places=2, null=True, blank=True)
    start_time = models.TimeField("Время начало", null=True, blank=True)
    end_time = models.TimeField("Время конец", null=True, blank=True)
    is_per_day = models.BooleanField("За сутки", default=False)

    def __str__(self):
        return self.title
    
    def clean(self):
        super().clean()
        if self.max_price and self.max_price < self.price:
            raise ValidationError({'max_price':"Цена не должна быть меньше основной цены"})
    
    class Meta:
        verbose_name = "Дополнительная услуга"
        verbose_name_plural = "Дополнительные услуги"


class PricingPlan(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name="plans", verbose_name="Машина")
    season = models.ForeignKey(Season, on_delete=models.CASCADE, verbose_name="Сезон")
    min_day = models.PositiveIntegerField("Минимальный день")
    max_day = models.PositiveIntegerField("Максимальный день", null=True, blank=True)
    price_period = models.DecimalField("Цена периода", decimal_places=2, max_digits=15)
    extra_service = models.ManyToManyField(ExtraService, blank=True)
    is_active = models.BooleanField("Активна", default=True)

    def __str__(self):
        return str(self.car)
    
    def clean(self):
        super().clean()

        if self.max_day and self.max_day <= self.min_day:
            raise ValidationError({'max_day':"Максимальный день должен быть больше минимального дня"})
    
    class Meta:
        verbose_name = "План цены"
        verbose_name_plural = "План цен"



