from django.urls import path
from .views import *

urlpatterns = [
    path('banners/', BannerView.as_view()),
    path('benefits/', BenefitView.as_view()),
    path('comments/', CommentView.as_view()),
    path('contacts/', ContactView.as_view()),
]