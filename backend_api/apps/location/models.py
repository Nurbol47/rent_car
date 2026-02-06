from django.db import models
from apps.car.models import Car

class Location(models.Model):
    """
    Модель точек проката. Связана с Car через ManyToMany для гибкого 
    управления автопарком в разных регионах.
    """
    cars = models.ManyToManyField(
        Car, 
        related_name="locations", 
        verbose_name="Доступные машины"
    )
    title = models.CharField("Название", max_length=200)
    img = models.ImageField("Изображение", upload_to="location_img/")
    description = models.TextField("Описание")

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Локация"
        verbose_name_plural = "Локации"


class Characteristic(models.Model):
    """
    Дополнительные параметры локации. Используется ForeignKey для 
    динамического расширения описания (адрес, телефон, режим работы).
    """
    location = models.ForeignKey(
        Location, 
        on_delete=models.CASCADE, 
        verbose_name="Локация", 
        related_name="characteristics"
    )
    title = models.CharField("Название", max_length=200)
    parameter = models.CharField("Параметры", max_length=100)

    def __str__(self):
        return f"{self.title}: {self.parameter}"
    
    class Meta:
        verbose_name = "Характеристика" 
        verbose_name_plural = "Характеристики"