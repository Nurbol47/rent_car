from rest_framework import generics
from .models import Location, BaseLocation
from .serializers import LocationSerializer, LocationDetailSerializer, CharacteristicSerializer, BaseLocationSerializer


class BaseLocationView(generics.ListAPIView):
    """
    Список базовых локаций (регионов).
    Служит для фильтрации основных локаций.
    """
    queryset = BaseLocation.objects.all()
    serializer_class = BaseLocationSerializer


class LocationView(generics.ListAPIView):
    """
    Список локаций (краткая информация). 
    Используется для начального отображения доступных офисов.
    """
    queryset = Location.objects.all().prefetch_related('img')
    serializer_class = LocationSerializer


class LocationDetailView(generics.RetrieveAPIView):
    """
    Детальная информация о локации.
    Использует prefetch_related для исключения проблемы N+1 при загрузке 
    вложенных характеристик и списка машин.
    """
    # prefetch_related объединяет запросы к ManyToMany и ForeignKey в один эффективный SQL-запрос
    queryset = Location.objects.all().prefetch_related('characteristics', 'cars', 'img')
    serializer_class = LocationDetailSerializer