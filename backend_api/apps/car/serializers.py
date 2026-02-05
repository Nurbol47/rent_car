from rest_framework import serializers
from .models import *


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"


class CarDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['name', 'img', 'duration_start', 'duration_end', 'discount', 'total_price']


class BookCarSerializer(serializers.ModelSerializer):

    car = CarSerializer(read_only=True)

    class Meta:
        model = BookCar
        fields = "__all__"
        read_only_fields = ["car"]