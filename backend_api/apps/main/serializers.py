from rest_framework import serializers
from .models import Banner, Comment

class BannerSerializer(serializers.ModelSerializer):
    """Сериализатор для рекламных баннеров на главной странице"""
    class Meta:
        model = Banner
        fields = ['id', 'title', 'short_description', 'img', 'ordering']



class CommentSerializer(serializers.ModelSerializer):
    """
    Сериализатор отзывов пользователей.
    Автоматически подтягивает имя автора и формирует полный URL для аватара.
    """
    # Вывод имени вместо ID пользователя
    user_name = serializers.ReadOnlyField(source='user.first_name')
    user_avatar = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ['id', 'user_name', 'user_avatar', 'comment', 'rating']

    def get_user_avatar(self, obj):
        """Формирует абсолютный путь к изображению для корректного отображения на фронтенде"""
        request = self.context.get('request')
        if obj.img and request:
            return request.build_absolute_uri(obj.img.url)
        return None

