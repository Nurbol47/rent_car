from django.contrib import admin
from .models import Season, ExtraService, PricingPlan

@admin.register(Season)
class SeasonAdmin(admin.ModelAdmin):
    """Настройка отображения сезонов"""
    list_display = ['id', 'month_from', 'month_to']
    list_editable = ['month_from', 'month_to']


@admin.register(ExtraService)
class ExtraServiceAdmin(admin.ModelAdmin):
    """Управление дополнительными услугами"""
    list_display = ['title', 'price', 'max_price', 'is_per_day']
    list_filter = ['is_per_day']
    search_fields = ['title']


@admin.register(PricingPlan)
class PricingPlanAdmin(admin.ModelAdmin):
    """
    Комплексная панель управления тарифами.
    Оптимизирована для работы с ManyToMany связями.
    """
    list_display = [
        'car', 'season', 'min_day', 'max_day', 
        'price_period', 'get_extra_services', 'is_active'
    ]
    list_filter = ['is_active', 'season', 'car']
    list_editable = ['price_period', 'is_active']
    search_fields = ['car__brand', 'car__model']
    
    # Интерфейс для удобного выбора услуг в карточке
    filter_horizontal = ['extra_service']

    def get_extra_services(self, obj):
        """Отображение списка услуг через запятую"""
        return ", ".join([s.title for s in obj.extra_service.all()]) or "—"
    
    get_extra_services.short_description = "Включенные услуги"

    def get_queryset(self, request):
        """Оптимизация: подгружаем машину, сезон и услуги одним запросом"""
        return super().get_queryset(request).select_related('car', 'season').prefetch_related('extra_service')