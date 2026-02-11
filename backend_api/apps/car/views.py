from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .filters import CarFilter
from .models import Car, BookCar, UserModel
from .serializers import CarSerializer, CarDetailSerializer, BookCarSerializer, UserModelSerializer

class CarView(generics.ListAPIView):
    """
    Представление для получения полного списка автомобилей.
    Возвращает список всех машин, отсортированный по марке и модели.
    """
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    
    # Подключаем бэкенды фильтрации и сортировки
    filter_backends = [
        DjangoFilterBackend, 
        filters.OrderingFilter, 
        filters.SearchFilter
    ]
    
    # Привязываем наш кастомный фильтр
    filterset_class = CarFilter
    
    # Настраиваем сортировку (для кнопок "Дороже", "Дешевле", "Со скидкой")
    ordering_fields = ['discount', 'year_of_manufacture'] 
    
    def get_queryset(self):
        # Оставляем базовую сортировку, если фильтры не применены
        return super().get_queryset().order_by('brand', 'model')


class CarDetailView(generics.RetrieveAPIView):
    """
    Представление для получения детальной информации о конкретном автомобиле.
    Используется для страницы автомобиля (поиск по ID/Primary Key).
    """
    queryset = Car.objects.all()
    serializer_class = CarDetailSerializer


class BookCarView(generics.ListCreateAPIView):
    """
    Представление для работы с бронированиями.
    - GET: Возвращает историю бронирований текущего авторизованного пользователя.
    - POST: Создает новую заявку на бронирование.
    """
    serializer_class = BookCarSerializer

    def get_queryset(self):
        """
        Возвращает бронирования только текущего пользователя.
        Использует select_related для оптимизации SQL-запросов (JOIN с таблицей Car).
        """
        return BookCar.objects.filter(
            user=self.request.user
        ).select_related('car').prefetch_related('contact_info').order_by('-call_time')


class UserModelView(generics.ListCreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserModelSerializer