from django.db import models
from apps.car.models import Car


class Location(models.Model):
    cars = models.ManyToManyField(Car, verbose_name="Машины")
    title = models.CharField("Название", max_length=200)
    img = models.ImageField("Изображение", upload_to="location_img/")
    description = models.TextField("Описание")

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Локация"
        verbose_name_plural = "Локации"


class Characteristic(models.Model):
    location = models.ForeignKey(
        Location, 
        on_delete=models.SET_NULL, 
        verbose_name="Локация", 
        null=True, blank=True, 
        related_name="characteristics")
    title = models.CharField("Название", max_length=200)
    parameter = models.CharField("Параметры", max_length=100)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Характеристика" 
        verbose_name_plural = "Характеристики"
        