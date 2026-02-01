from django.urls import path
from .views import *

urlpatterns = [
    path('booking_car/', BookCarView.as_view()),
]