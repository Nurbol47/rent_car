from django.urls import path
from .views import *

urlpatterns = [
    path('pricing-plan/', PricingPlanView.as_view()),
#     path('booking_cars/', BookCarView.as_view()),
#     path('cars/', CarView.as_view()),
#     path('pricing-plan/', PricingPlanView.as_view()),
]