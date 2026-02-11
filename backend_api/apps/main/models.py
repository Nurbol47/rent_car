from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator

class Banner(models.Model):
    """
    Рекламные баннеры для главной страницы.
    Позволяет управлять слайдером через поле ordering.
    """
    title = models.CharField("Заголовок", max_length=200)
    short_description = models.TextField("Краткое описание")
    img = models.ImageField("Изображение", upload_to="main_imgs/")
    ordering = models.PositiveSmallIntegerField("Порядок сортировки", default=0)
    is_active = models.BooleanField("Статус отображения", default=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Баннер"
        verbose_name_plural = "Баннеры"
        ordering = ['ordering', 'id']



class Comment(models.Model):
    """
    Отзывы клиентов. 
    Включает систему рейтинга и привязку к профилю пользователя.
    """
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name="comments",
        verbose_name="Автор"
    )
    img = models.ImageField("Аватар пользователя", upload_to="user_imgs/", null=True, blank=True)
    comment = models.TextField("Текст отзыва")
    rating = models.PositiveSmallIntegerField(
        "Рейтинг (1-5)",
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        help_text="Оценка качества обслуживания"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return f"Отзыв от {self.user} ({self.rating}/5)"
    
    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
        ordering = ['-created_at']


