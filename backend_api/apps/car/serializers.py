from rest_framework import serializers
from django.db import transaction
from .models import Car, CarWashOption, BookCar, UserModel, ImgCar


class ImgCarSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImgCar
        fields = ['img']


class CarSerializer(serializers.ModelSerializer):
    """
    Базовый сериализатор для модели Car.
    Используется для полного представления данных об автомобиле.
    """
    old_price = serializers.IntegerField(source='get_current_price', read_only=True)
    total_price = serializers.IntegerField(source='get_discounted_price', read_only=True)
    promo_period = serializers.SerializerMethodField()
    img = ImgCarSerializer(many=True, read_only=True)

    class Meta:
        model = Car
        fields = [
            'id', 'name', 'img', 'discount', 'old_price', 
            'duration_start', 'duration_end', 'total_price', 'promo_period',
            'seating', 'drive_unit', 'fuel_type' # Добавлено для отображения в списке
        ]

    def get_promo_period(self, obj):
        """Формирует строку дат для желтой плашки из Figma"""
        if obj.duration_start and obj.duration_end:
            start = obj.duration_start.strftime('%d.%m')
            end = obj.duration_end.strftime('%d.%m')
            return f"{start} - {end}"
        return None


class CarDetailSerializer(serializers.ModelSerializer):
    """
    Упрощенный сериализатор для отображения краткой информации о машине.
    Оптимизирован для использования в списках и вложенных объектах.
    """
    old_price = serializers.IntegerField(source='get_current_price', read_only=True)
    total_price = serializers.IntegerField(source='get_discounted_price', read_only=True)
    img = ImgCarSerializer(many=True, read_only=True)

    class Meta:
        model = Car
        fields = [
            'id', 'name', 'img', 'brand', 'model', 
            'color', 'drive_unit', 'body_car', 
            'year_of_manufacture', 'discount', 'pledge',
            'seating', 'engine_power', 'fuel_type',
            'old_price', 'total_price', 'duration_start', 'duration_end'
        ]

class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['id', 'full_name', 'phone', 'agreement', 'booking']
        extra_kwargs = {'booking': {'required': False}}

    def validate_agreement(self, value):
        if not value:
            raise serializers.ValidationError("Необходимо согласие на обработку данных.")
        return value


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

    contact_info = UserModelSerializer(required=False)
    
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
            'is_city', 'is_airport', 'call_time', 'status', 'contact_info'
        ]
        # Поля, которые рассчитываются сервером и не могут быть изменены клиентом
        read_only_fields = ['total_price_snapshot', 'call_time']

    def validate(self, attrs):
        """
        Валидация дат на уровне сериализатора для возврата 
        клиенту понятной ошибки 400 Bad Request.
        """
        start = attrs.get('duration_start')
        end = attrs.get('duration_end')
        car = attrs.get('car')  # Получаем объект машины из source='car'
        
        if not car and self.instance:
            car = self.instance.car

        if start and end:
            if start >= end:
                raise serializers.ValidationError({
                    "duration_end": "Дата окончания должна быть позже даты начала."
                })
            
            # Проверка на пересечение бронирований (аналог логики в модели)
            if car:
                overlap = BookCar.objects.filter(
                    car=car,
                    status__in=['pending', 'confirmed'],
                    duration_start__lt=end,
                    duration_end__gt=start
                )
                # Если мы обновляем существующее бронирование, исключаем его из проверки
                if self.instance:
                    overlap = overlap.exclude(pk=self.instance.pk)

                if overlap.exists():
                    raise serializers.ValidationError("Машина уже забронирована на выбранный период.")

        return attrs

    def create(self, validated_data):
        contact_data = validated_data.pop('contact_info', None)
        
        with transaction.atomic():
            booking = BookCar.objects.create(**validated_data)
            
            if contact_data:
                UserModel.objects.create(booking=booking, **contact_data)
            
        return booking
    
