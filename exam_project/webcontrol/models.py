from django.contrib.auth.models import User  # Импортируем встроенную модель User
from django.db import models


class DzExam(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название экзамена")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания записи")
    exam_date = models.DateField(verbose_name="Дата проведения экзамена")
    exam_image = models.ImageField(upload_to='exam_images/', blank=True, null=True, verbose_name="Изображение задания")
    examinees = models.ManyToManyField(User, verbose_name="Пользователи, пишущие экзамен")
    is_public = models.BooleanField(default=False, verbose_name="Опубликовано")

    class Meta:
        verbose_name = "Экзамен ДЗ"
        verbose_name_plural = "Экзамены ДЗ"

    def __str__(self):
        return self.title
