from django.urls import path
from .views import PricingPlanView

urlpatterns = [
    # Список всех активных тарифных планов
    path('pricing-plans/', PricingPlanView.as_view(), name='pricing-plan-list'),
]