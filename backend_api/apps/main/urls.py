from django.urls import path
from .views import *

urlpatterns = [
    path('banners/', BannerView.as_view()),
    path('comments/', CommentView.as_view()),
]