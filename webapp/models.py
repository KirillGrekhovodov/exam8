from django.contrib.auth import get_user_model
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import Avg

CHOISES = [('other', 'Разное'), ('phones', 'Телефоны'), ('headphones', 'Наушники'), ('cases', 'Чехол')]


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    category = models.CharField(max_length=20, default='other', choices=CHOISES, verbose_name='Категории')
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Описание')
    picture = models.ImageField(verbose_name='Картинка', upload_to='pictures', null=True, blank=True)

    class Meta:
        db_table = "products"
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return f"{self.name} - {self.category}"

    def get_avg(self):
        result = self.reviews.filter(is_moderated=True).aggregate(avg=Avg("mark"))
        return result["avg"]


class Review(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='reviews', verbose_name='Автор')
    product = models.ForeignKey('webapp.Product', on_delete=models.CASCADE, related_name='reviews',
                                verbose_name='Товар')
    text = models.TextField(max_length=2000, verbose_name='Текст отзыва')
    mark = models.IntegerField(verbose_name='Оценка', validators=[MaxValueValidator(5), MinValueValidator(1)])
    is_moderated = models.BooleanField(verbose_name='Подтвержден', default=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    edited_at = models.DateTimeField(auto_now=True, verbose_name='Дата редактирования')

    class Meta:
        db_table = "reviews"
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        permissions = [("view_not_moderated_review", "Видеть немодерированные отзывы")]

    def __str__(self):
        return f"{self.author.username} - {self.product.name}"
