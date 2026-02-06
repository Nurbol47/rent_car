from rest_framework import serializers
from .models import Car, CarWashOption, BookCar

class CarSerializer(serializers.ModelSerializer):
    """
    Базовый сериализатор для модели Car.
    Используется для полного представления данных об автомобиле.
    """
    class Meta:
        model = Car
        fields = "__all__"


class CarDetailSerializer(serializers.ModelSerializer):
    """
    Упрощенный сериализатор для отображения краткой информации о машине.
    Оптимизирован для использования в списках и вложенных объектах.
    """
    class Meta:
        model = Car
        fields = ['id', 'name', 'img', 'brand', 'model', 'discount', 'pledge']


class BookCarSerializer(serializers.ModelSerializer):
    """
    Основной сериализатор для процесса бронирования.
    Реализует разделение логики: детальное отображение машины при чтении (GET)
    и прием только ID объектов при записи (POST/PATCH).
    """
    
    # Вложенное представление машины (только для чтения)
    car = CarDetailSerializer(read_only=True)
    
    # Автоматическая привязка текущего авторизованного пользователя
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    
    # Поля для записи (принимают ID), связываются с оригинальными полями через 'source'
    car_id = serializers.PrimaryKeyRelatedField(
        queryset=Car.objects.all(), 
        source='car', 
        write_only=True,
        help_text="ID автомобиля для бронирования"
    )
    
    has_wash_type_id = serializers.PrimaryKeyRelatedField(
        queryset=CarWashOption.objects.all(),
        source='has_wash_type',
        write_only=True,
        required=False,
        help_text="ID выбранного типа мойки"
    )

    class Meta:
        model = BookCar
        fields = [
            'id', 'user', 'car', 'car_id', 'duration_start', 'duration_end', 
            'total_price_snapshot', 'child_seat', 'has_wash_type', 
            'has_wash_type_id', 'is_wish', 'car_delivery', 
            'is_city', 'is_airport', 'call_time', 'status'
        ]
        # Поля, которые рассчитываются сервером и не могут быть изменены клиентом
        read_only_fields = ['total_price_snapshot', 'call_time']

    def validate(self, attrs):
        """
        Валидация дат на уровне сериализатора для возврата 
        клиенту понятной ошибки 400 Bad Request.
        """
        if attrs.get('duration_start') and attrs.get('duration_end'):
            if attrs.get('duration_start') >= attrs.get('duration_end'):
                raise serializers.ValidationError({
                    "duration_end": "Дата окончания должна быть позже даты начала."
                })
        return attrs