from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render, reverse
import os


def home_view(request):
    template_name = 'app/home.html'
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('current_time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }

    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    current_times = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    msg = f'Текущее время: {current_times}'
    return HttpResponse(msg)


def workdir_view(request):
    files = os.listdir('.')
    files_list = '<br>'.join(files)
    return HttpResponse(f'Содержимое рабочей директории:<br>{files_list}')
