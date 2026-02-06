from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Car, BookCar
from .serializers import CarSerializer, BookCarSerializer

class CarView(generics.ListAPIView):
    """
    Представление для получения полного списка автомобилей.
    Возвращает список всех машин, отсортированный по марке и модели.
    """
    queryset = Car.objects.all().order_by('brand', 'model')
    serializer_class = CarSerializer


class CarDetailView(generics.RetrieveAPIView):
    """
    Представление для получения детальной информации о конкретном автомобиле.
    Используется для страницы автомобиля (поиск по ID/Primary Key).
    """
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class BookCarView(generics.ListCreateAPIView):
    """
    Представление для работы с бронированиями.
    - GET: Возвращает историю бронирований текущего авторизованного пользователя.
    - POST: Создает новую заявку на бронирование.
    """
    serializer_class = BookCarSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Возвращает бронирования только текущего пользователя.
        Использует select_related для оптимизации SQL-запросов (JOIN с таблицей Car).
        """
        return BookCar.objects.filter(
            user=self.request.user
        ).select_related('car').order_by('-call_time')
    
    def perform_create(self, serializer):
        """
        Автоматически назначает текущего пользователя владельцем бронирования
        в процессе сохранения объекта.
        """
        serializer.save(user=self.request.user)