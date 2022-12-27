from django.shortcuts import render


def index(request):
    """ Главная страница, без основного подарка """
    return render(request, 'index.html', locals())