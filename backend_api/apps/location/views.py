from django.shortcuts import render
from rest_framework import generics
from .serializers import LocationSerializer, LocationDetailSerializer
from .models import Location


class LocationView(generics.ListAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class LocationDetailView(generics.RetrieveAPIView):
    queryset = Location.objects.all().prefetch_related('characteristics', 'cars')
    serializer_class = LocationDetailSerializer

