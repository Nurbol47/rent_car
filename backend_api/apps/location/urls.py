from django.urls import path
from .views import LocationView, LocationDetailView


urlpatterns = [
    path('', LocationView.as_view()),
    path('location-detail/<int:pk>/', LocationDetailView.as_view()),
]