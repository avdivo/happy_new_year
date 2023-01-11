from django.shortcuts import render
from django.http import JsonResponse

from .models import Prediction, Message

import random


def index(request, id_mes=0):
    """ Главная страница без основного подарка,
        если передан параметр, то только с основным подарком и текстом сообщения"""
    message = ''
    if id_mes:
        try:
            message = Message.objects.get(id=id_mes).message
        except:
            id_mes = 0  # Если сообщения с таким id не существует, выводим простую стартовую страницу
    return render(request, 'index.html', locals())


def save_mess(request):
    """ Страница для получения сообщения
        Вернет url сервера с uuid сообщения """
    id = Message.objects.create(message=request.POST.get('message')).id
    return JsonResponse({'url': request.build_absolute_uri()[:-10] + str(id)})


def prediction(request):
    """ Выбор предсказания для Ajax запроса по присланному номеру подарка """
    gift = int(request.POST.get('number_gift'))
    le = len(Prediction.objects.all())
    pr = [random.randint(1, le) for _ in range(gift)][-1]
    prediction = Prediction.objects.get(pk=pr)
    return JsonResponse({'prediction': prediction.prediction})
