# exam_project/exam_project/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings # Для настройки обработки медиафайлов
from django.conf.urls.static import static # Для настройки обработки медиафайлов

urlpatterns = [
    path('admin/', admin.site.urls),
    path('webcontrol/', include('webcontrol.urls')), # <-- Добавьте эту строку
]

# Добавляем обработку медиафайлов для режима разработки
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)