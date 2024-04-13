import os
from datetime import datetime

from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, reverse


def home_view(request: HttpRequest) -> HttpResponse:
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }

    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request: HttpRequest) -> HttpResponse:
    # обратите внимание – здесь HTML шаблона нет, 
    # возвращается просто текст
    now = datetime.now()
    current_time = now.strftime("%d-%m-%Y %H:%M")
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request: HttpRequest) -> HttpResponse:
    # по аналогии с `time_view`, напишите код,
    # который возвращает список файлов в рабочей 
    # директории
    list_files = os.listdir(path='.')

    if not list_files:
        raise NotImplemented
    str_files = '<br>'.join(list_files)
    print(str_files)
    return HttpResponse(str_files)
