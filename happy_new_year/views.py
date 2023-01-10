from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse, HttpRequest

from .models import Prediction

import random


def index(request, id_mes=0):
    """ Главная страница без основного подарка,
        если передан параметр, то только с основным подарком и текстом сообщения"""

    return render(request, 'index.html', locals())


def save_mess(request):
    """ Страница для получения сообщения """
    # print(request.POST.get('message'))
    return render(request, 'index.html', locals())


def prediction(request):
    """ Выбор предсказания для Ajax запроса по присланному номеру подарка """
    gift = int(request.POST.get('number_gift'))
    le = len(Prediction.objects.all())
    pr = [random.randint(1, le) for _ in range(gift)][-1]
    prediction = Prediction.objects.get(pk=pr)
    return JsonResponse({'prediction': prediction.prediction})
