from django.shortcuts import render
from rest_framework import generics
from .serializers import *

class CarView(generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class BookCarView(generics.ListCreateAPIView):
    queryset = BookCar.objects.all()
    serializer_class = BookCarSerializer

