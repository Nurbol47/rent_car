from rest_framework import serializers
from .models import Location, Characteristic
from apps.car.serializers import CarDetailSerializer

class CharacteristicSerializer(serializers.ModelSerializer):
    """
    Сериализатор для характеристик локации (адрес, контакты и т.д.).
    """
    class Meta:
        model = Characteristic
        fields = ['id', 'title', 'parameter']


class LocationSerializer(serializers.ModelSerializer):
    """
    Краткое представление локации для общего списка.
    Используется для минимизации объема передаваемых данных.
    """
    class Meta:
        model = Location
        fields = ['id', 'title', 'img']


class LocationDetailSerializer(serializers.ModelSerializer):
    """
    Полное представление локации.
    Включает связанные характеристики и список доступных автомобилей.
    """
    # many=True обязателен, так как это связи ForeignKey и ManyToMany
    characteristics = CharacteristicSerializer(many=True, read_only=True)
    cars = CarDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Location
        fields = ['id', 'title', 'img', 'description', 'characteristics', 'cars']