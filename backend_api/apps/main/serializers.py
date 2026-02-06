from rest_framework import serializers
from .models import Banner, Benefit, Comment, Contact

class BannerSerializer(serializers.ModelSerializer):
    """Сериализатор для рекламных баннеров на главной странице"""
    class Meta:
        model = Banner
        fields = ['id', 'title', 'short_description', 'img', 'ordering']


class BenefitSerializer(serializers.ModelSerializer):
    """Сериализатор преимуществ компании"""
    class Meta:
        model = Benefit
        fields = ['id', 'icon', 'title', 'description']


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


class ContactSerializer(serializers.ModelSerializer):
    """Сериализатор контактной информации и ссылок на соцсети"""
    class Meta:
        model = Contact
        fields = [
            'id', 'full_name', 'phone_number', 'email', 
            'address', 'instagram', 'whatsapp', 'telegram'
        ]