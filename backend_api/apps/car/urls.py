from django.urls import path
from .views import *

urlpatterns = [
    path('cars/', CarView.as_view()),
    path('booking-cars/', BookCarView.as_view()),
]