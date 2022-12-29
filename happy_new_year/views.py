from django.shortcuts import render


def index(request):
    """ Главная страница, без основного подарка """
    return render(request, 'index.html', locals())


def prediction(request):
    """ Выбор предсказания для Ajax запроса по присланному номеру подарка """
    print(request, '------------------------------')
    return render(request, 'index.html', locals())