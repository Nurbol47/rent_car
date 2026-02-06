from rest_framework import generics
from .models import PricingPlan
from .serializers import PricingPlanSerializer

class PricingPlanView(generics.ListAPIView):
    """
    Возвращает список всех тарифных планов.
    Использует оптимизацию запросов для подгрузки связанных сезонов и доп. услуг.
    """
    # select_related для ForeignKey (Season), prefetch_related для ManyToMany (ExtraService)
    queryset = PricingPlan.objects.filter(is_active=True).select_related(
        'season'
    ).prefetch_related(
        'extra_service'
    )
    serializer_class = PricingPlanSerializer