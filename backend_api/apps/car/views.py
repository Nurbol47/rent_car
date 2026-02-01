from django.shortcuts import render
from rest_framework import generics
from .serializers import *


class BookCarView(generics.CreateAPIView):
    queryset = BookCar.objects.all()
    serializer_class = BookCarSerializer
