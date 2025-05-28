# exam_project/webcontrol/admin.py

from django.contrib import admin
from .models import DzExam

class DzExamAdmin(admin.ModelAdmin):
    search_fields = ('title', 'examinees__email')

    date_hierarchy = 'exam_date'

    filter_horizontal = ('examinees',)

    list_filter = ('is_public', 'created_at', 'exam_date')

    list_display = ('title', 'exam_date', 'is_public', 'created_at', 'display_examinees')

    def display_examinees(self, obj):
        return ", ".join([user.get_full_name() or user.username for user in obj.examinees.all()])
    display_examinees.short_description = "Студенты"

admin.site.register(DzExam, DzExamAdmin)