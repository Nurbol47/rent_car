from rest_framework import generics
from rest_framework.response import Response
from .models import Banner, Benefit, Comment, Contact
from .serializers import (
    BannerSerializer, BenefitSerializer, 
    CommentSerializer, ContactSerializer
)

class BannerView(generics.ListAPIView):
    """
    Возвращает список активных баннеров для слайдера на главной странице.
    Сортировка задана в Meta модели (по полю ordering).
    """
    queryset = Banner.objects.filter(is_active=True)
    serializer_class = BannerSerializer


class BenefitView(generics.ListAPIView):
    """Список преимуществ компании (УТП)"""
    queryset = Benefit.objects.all()
    serializer_class = BenefitSerializer


class CommentView(generics.ListAPIView):
    """
    Список отзывов пользователей. 
    Рекомендуется использовать select_related для оптимизации запроса к автору (User).
    """
    queryset = Comment.objects.all().select_related('user')
    serializer_class = CommentSerializer


class ContactView(generics.ListAPIView):
    """
    Возвращает актуальную контактную информацию компании.
    Реализован возврат одного (первого) объекта вместо списка.
    """
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def list(self, request, *args, **kwargs):
        # Контакты обычно хранятся в единственном экземпляре
        instance = self.get_queryset().first()

        if instance:
            serializer = self.get_serializer(instance)
            return Response(serializer.data)

        # Возвращаем пустой объект, если контакты еще не заполнены
        return Response({}, status=200)