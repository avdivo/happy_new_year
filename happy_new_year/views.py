from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse, HttpRequest

from .models import Prediction

import random

def index(request):
    """ Главная страница, без основного подарка """
    return render(request, 'index.html', locals())


def get_mes(request, id_mes):
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
