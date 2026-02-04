from rest_framework import serializers
from .models import *


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"


class BookCarSerializer(serializers.ModelSerializer):

    car = CarSerializer(read_only=True)

    class Meta:
        model = BookCar
        fields = "__all__"
        read_only_fields = ["car"]