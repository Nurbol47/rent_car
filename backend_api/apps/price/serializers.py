from rest_framework import serializers
from .models import *


class SeasonSerializer(serializers.ModelSerializer):
    
    month_from = serializers.CharField(source='get_month_from_display', read_only=True)
    month_to = serializers.CharField(source='get_month_to_display', read_only=True)

    class Meta:
        model = Season
        fields = "__all__"


class ExtraSeriviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtraService
        fields = "__all__"


class PricingPlanSerializer(serializers.ModelSerializer):
    
    season = SeasonSerializer(read_only=True)
    extra_service = ExtraSeriviceSerializer(many=True, read_only=True)

    class Meta:
        model = PricingPlan
        fields = ["season", "min_day", "max_day", "price_period", "is_active", "extra_service"]
        read_only_fields = ["season", "extra_service"]




