# exam_project/webcontrol/admin.py

from django.contrib import admin
from .models import DzExam # Импортируем нашу модель DzExam

class DzExamAdmin(admin.ModelAdmin):
    # 1. Добавить поиск по названию экзамена и email пользователя
    search_fields = ('title', 'examinees__email')

    # 2. Добавить поиск по конкретной дате проведения экзамена (под строкой поиска)
    date_hierarchy = 'exam_date'

    # 3. Настроить удобное редактирование поля M2M (слева все возможные варианты, справа - привязанные к записи)
    filter_horizontal = ('examinees',)

    # 4. Фильтр по полю is_public
    # 5. Фильтр по полю даты добавления записи
    list_filter = ('is_public', 'created_at', 'exam_date')

    # Поля, которые будут отображаться в списке записей в админке
    list_display = ('title', 'exam_date', 'is_public', 'created_at', 'display_examinees')

    # Метод для отображения списка пользователей в list_display
    def display_examinees(self, obj):
        return ", ".join([user.get_full_name() or user.username for user in obj.examinees.all()])
    display_examinees.short_description = "Студенты"

admin.site.register(DzExam, DzExamAdmin)