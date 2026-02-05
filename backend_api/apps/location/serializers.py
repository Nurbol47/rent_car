from rest_framework import serializers
from .models import Location, Characteristic
from apps.car.serializers import CarDetailSerializer


class CharacteristicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Characteristic
        fields = ['title', 'parameter']


class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = ['img', 'title']


class LocationDetailSerializer(serializers.ModelSerializer):

    characteristics = CharacteristicSerializer(read_only=True, many=True)
    cars = CarDetailSerializer(read_only=True, many=True)

    class Meta:
        model = Location
        fields = ['img', 'title', 'characteristics', 'description', 'cars']