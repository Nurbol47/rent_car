from django.db import models
from apps.car.models import Car


class BaseLocation(models.Model):
    title = models.CharField("Название", max_length=200)
    img = models.ImageField("Изображение", upload_to="base_location_img/")

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Базовая локация"
        verbose_name_plural = "Базовые локации"


class Location(models.Model):
    """
    Модель точек проката. Связана с Car через ManyToMany для гибкого 
    управления автопарком в разных регионах.
    """
    base_location = models.ForeignKey(BaseLocation, on_delete=models.CASCADE, verbose_name="Базовая локация")
    cars = models.ManyToManyField(
        Car, 
        related_name="locations", 
        verbose_name="Доступные машины"
    )
    title = models.CharField("Название", max_length=200)
    description = models.TextField("Описание")

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Основная локация"
        verbose_name_plural = "Основные локации"


class ImgLocation(models.Model):
    location = models.ForeignKey(
        Location, 
        on_delete=models.CASCADE, 
        related_name='img',
        verbose_name="Локация", )
    img = models.ImageField("Изображение", upload_to="location_img/")

    class Meta:
        verbose_name = "Изображение локации"
        verbose_name_plural = "Изображения локации"

    def __str__(self):
        return self.img.name



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