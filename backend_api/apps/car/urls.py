from django.urls import path
from .views import CarView, CarDetailView, BookCarView, UserModelView

urlpatterns = [
    path('', CarView.as_view(), name='car-list'),
    path('car/<int:pk>/', CarDetailView.as_view(), name='car-detail'),
    path('booking-cars/', BookCarView.as_view(), name='booking-list-create'),
    path('user-model/', UserModelView.as_view(), name="user-model")
]