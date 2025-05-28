
from django.shortcuts import render
from .models import DzExam

def dz_exam_list(request):

    published_exams = DzExam.objects.filter(is_public=True).order_by('-exam_date')
    context = {
        'full_name': 'Дмитрий Закс',
        'group_number': 'Группа 241-671', # Замените на номер вашей группы
        'exams': published_exams
    }

    return render(request, 'webcontrol/dzexam_list.html', context)