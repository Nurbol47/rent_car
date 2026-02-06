from django.urls import path
from .views import CarView, CarDetailView, BookCarView

urlpatterns = [
    path('/', CarView.as_view(), name='car-list'),
    path('cars/<int:pk>/', CarDetailView.as_view(), name='car-detail'),
    path('booking-cars/', BookCarView.as_view(), name='booking-list-create'),
]