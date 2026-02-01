from rest_framework import serializers
from .models import *


class BookCarSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookCar
        fields = "__all__"