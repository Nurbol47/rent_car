from django.contrib import admin
from .models import *


@admin.register(Season)
class SeasonAdmin(admin.ModelAdmin):
    list_display = ['month_from', 'month_to']


@admin.register(ExtraService)
class ExtraServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'max_price', 'start_time', 'end_time', 'is_per_day']


@admin.register(PricingPlan)
class PricingPlanAdmin(admin.ModelAdmin):
    list_display = ['season', 'min_day', 'max_day', 'price_period', 'get_extra_service', 'is_active']

    def get_extra_service(self, obj):
        titles = [service.title for service in obj.extra_service.all()]
        return ", ".join(titles) if titles else "нет услуг"
    
    get_extra_service.short_description = "extra_service"

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('extra_service')



