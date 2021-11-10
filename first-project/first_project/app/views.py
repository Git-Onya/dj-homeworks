from datetime import datetime
from os import listdir

from django.http import HttpResponse
from django.shortcuts import render, reverse


def home_view(request):
    template_name = 'app/home.html'
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }

    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    current_time = datetime.now()
    msg = f'Текущее время: {current_time.strftime("%H:%M")}'
    return HttpResponse(msg)


def workdir_view(request):
    files_list = listdir()
    msg = f'В рабочей директории находятся следующие файлы: {files_list}'
    return HttpResponse(msg)
