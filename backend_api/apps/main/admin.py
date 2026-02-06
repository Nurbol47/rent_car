from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Banner, Benefit, Comment, Contact

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    """Управление рекламными баннерами с предпросмотром изображений"""
    list_display = ['preview', 'title', 'ordering', 'is_active']
    list_editable = ['ordering', 'is_active']
    list_filter = ['is_active']
    readonly_fields = ['preview']

    def preview(self, obj):
        """Метод для генерации HTML-тега изображения в списке и карточке"""
        if obj.img:
            return mark_safe(f'<img src="{obj.img.url}" style="max-height: 50px; border-radius: 5px;">')
        return "Нет изображения"
    
    preview.short_description = "Миниатюра"


@admin.register(Benefit)
class BenefitAdmin(admin.ModelAdmin):
    """Управление списком преимуществ (УТП)"""
    list_display = ['preview_icon', 'title']

    def preview_icon(self, obj):
        """Отображение иконки преимущества"""
        if obj.icon:
            return mark_safe(f'<img src="{obj.icon.url}" style="max-height: 30px;">')
        return "—"
    
    preview_icon.short_description = "Иконка"


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """Модерация отзывов пользователей"""
    list_display = ['user', 'rating', 'get_short_comment']
    list_filter = ['rating', 'user']
    # Позволяет быстро находить пользователя без загрузки тяжелого выпадающего списка
    raw_id_fields = ['user']

    def get_short_comment(self, obj):
        """Обрезает длинные комментарии для компактного вида в списке"""
        return obj.comment[:50] + "..." if len(obj.comment) > 50 else obj.comment
    
    get_short_comment.short_description = "Текст отзыва"


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """Управление контактными данными организации"""
    list_display = ['full_name', 'phone_number', 'email', 'address']
    
    # Запрещаем создание более чем одной записи, если это Singleton
    def has_add_permission(self, request):
        return not Contact.objects.exists()