import django_filters
from .models import Car, BookCar
from django.db.models import Exists, OuterRef

class CarFilter(django_filters.FilterSet):
    # 1. Исправляем [invalid name]: добавляем label для кастомных методов
    date_start = django_filters.DateFilter(
        method='filter_availability', 
        label="Дата начала"
    )
    date_end = django_filters.DateFilter(
        method='filter_availability', 
        label="Дата конца"
    )

    # 2. Объявляем марку с человеческим названием
    brand = django_filters.CharFilter(lookup_expr='icontains', label="Марка")

    # 3. Исправляем дубль года выпуска: убираем лишнее свойство 'year'
    # Используем сразу правильное имя поля из модели
    year_of_manufacture = django_filters.NumberFilter(label="Год выпуска")

    # 4. Посадочные места (минимум)
    seating_min = django_filters.NumberFilter(
        field_name='seating', 
        lookup_expr='gte', 
        label="Посадочных мест (от)"
    )

    def filter_availability(self, queryset, name, value):
        if name != 'date_start':
            return queryset

        # Используем валидированные данные из формы, а не сырые строки из query_params
        start = self.form.cleaned_data.get('date_start')
        end = self.form.cleaned_data.get('date_end')

        if start and end:
            # Валидация: если даты некорректны (начало > конца), возвращаем пустой список
            if start >= end:
                return queryset.none()

            # 1. Проверяем, что даты аренды попадают в период действия объявления машины
            queryset = queryset.filter(
                duration_start__lte=start,
                duration_end__gte=end
            )

            # 2. Оптимизация: используем Exists вместо медленного 'id__in'
            # Создаем подзапрос, который ищет пересекающиеся бронирования для каждой машины
            overlapping_bookings = BookCar.objects.filter(
                car=OuterRef('pk'),
                status__in=['pending', 'confirmed'],
                duration_start__lt=end,
                duration_end__gt=start
            )
            # Аннотируем каждую машину (is_occupied=True/False) и фильтруем
            return queryset.annotate(is_occupied=Exists(overlapping_bookings)).filter(is_occupied=False)
        
        return queryset
    
    color = django_filters.CharFilter(lookup_expr='icontains', label="Цвет")
    drive_unit = django_filters.CharFilter(lookup_expr='iexact', label="Привод")
    
    # 3. Улучшение: делаем фильтр по мощности двигателя диапазоном "от" и "до"
    engine_power_min = django_filters.NumberFilter(field_name='engine_power', lookup_expr='gte', label="Мощность от (л.с.)")
    engine_power_max = django_filters.NumberFilter(field_name='engine_power', lookup_expr='lte', label="Мощность до (л.с.)")

    class Meta:
        model = Car
        # Добавляем новые поля в список
        fields = ['body_car']