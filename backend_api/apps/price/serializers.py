from rest_framework import serializers
from .models import Season, ExtraService, PricingPlan

class SeasonSerializer(serializers.ModelSerializer):
    """
    Сериализатор сезонов. 
    Преобразует числовые значения месяцев в человекочитаемые названия.
    """
    month_from = serializers.CharField(source='get_month_from_display', read_only=True)
    month_to = serializers.CharField(source='get_month_to_display', read_only=True)

    class Meta:
        model = Season
        fields = ['id', 'month_from', 'month_to']


class ExtraServiceSerializer(serializers.ModelSerializer):
    """Сериализатор дополнительных услуг (страховка, кресло и т.д.)"""
    class Meta:
        model = ExtraService
        fields = ['id', 'title', 'price', 'max_price', 'is_per_day', 'start_time', 'end_time']


class PricingPlanSerializer(serializers.ModelSerializer):
    """
    Комплексный сериализатор тарифного плана.
    Используется для отображения полных условий аренды в карточке авто.
    """
    season = SeasonSerializer(read_only=True)
    extra_service = ExtraServiceSerializer(many=True, read_only=True)

    class Meta:
        model = PricingPlan
        fields = [
            'id', 'season', 'min_day', 'max_day', 
            'price_period', 'is_active', 'extra_service'
        ]