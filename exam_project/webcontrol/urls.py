
from django.urls import path
from . import views

app_name = 'webcontrol'

urlpatterns = [
    path('dzexam/', views.dz_exam_list, name='dzexam_list'),
]