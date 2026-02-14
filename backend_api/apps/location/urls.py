from django.urls import path
from .views import LocationView, LocationDetailView, BaseLocationView


urlpatterns = [
    path('base-location/', BaseLocationView.as_view()),
    path('', LocationView.as_view()),
    path('location-detail/<int:pk>/', LocationDetailView.as_view()),
]