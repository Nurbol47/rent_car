from rest_framework import generics
from rest_framework.response import Response
from .models import Banner, Comment
from .serializers import (
    BannerSerializer, 
    CommentSerializer,
)

class BannerView(generics.ListAPIView):
    """
    Возвращает список активных баннеров для слайдера на главной странице.
    Сортировка задана в Meta модели (по полю ordering).
    """
    queryset = Banner.objects.filter(is_active=True)
    serializer_class = BannerSerializer


class CommentView(generics.ListAPIView):
    """
    Список отзывов пользователей. 
    Рекомендуется использовать select_related для оптимизации запроса к автору (User).
    """
    queryset = Comment.objects.all().select_related('user')
    serializer_class = CommentSerializer

