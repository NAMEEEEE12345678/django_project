# django_project
Документация Django-проекта

## 1. Описание проекта

Этот Django-проект управляет вакансиями, включая отображение списка вакансий и детальной информации о каждой из них.

2. Установка и запуск проекта

2.1 Установка зависимостей

pip install -r requirements.txt

2.2 Применение миграций

python manage.py migrate

2.3 Запуск сервера

python manage.py runserver

3. Структура проекта

3.1 Views (Представления)

Представления обрабатывают HTTP-запросы и возвращают ответы.

from django.shortcuts import render, get_object_or_404
from .models import Vacancy

def home(request):
    return render(request, 'home.html')

def vacancies_list(request):
    vacancies = Vacancy.objects.all()
    return render(request, "post_list.html", {"vacancies": vacancies})

def vacancy_detail(request, id):
    vacancy = get_object_or_404(Vacancy, id=id)
    return render(request, "vacancy_detail.html", {"vacancy": vacancy})

3.2 URL-конфигурация (urls.py)

Определяет маршруты проекта.

from django.urls import path
from .views import home, vacancies_list, vacancy_detail

urlpatterns = [
    path('', home, name='home_page'),
    path('vacancies/', vacancies_list, name='vacancies_list'),
    path('vacancy/<int:id>/', vacancy_detail, name='vacancy_detail'),
]

3.3 Модели (models.py)

Определяют структуру базы данных.

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Vacancy(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

3.4 Админ-панель (admin.py)

Позволяет управлять моделями через административный интерфейс.

from django.contrib import admin
from .models import Vacancy, Category

admin.site.register(Vacancy)
admin.site.register(Category)

3.5 ASGI-конфигурация (asgi.py)

Настройка асинхронного сервера.

import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

application = get_asgi_application()

4. Файлы настроек (settings.py)

Файл settings.py содержит ключевые параметры проекта, такие как:

База данных (DATABASES)

Установленные приложения (INSTALLED_APPS)

Настройки статических файлов (STATIC_URL)

### 5. Команды Django

python manage.py runserver – запуск сервера

python manage.py makemigrations – создание миграций

python manage.py migrate – применение миграций

python manage.py createsuperuser – создание администратора
