from django.shortcuts import render, redirect


def index(request):
    """ Главная страница, без основного подарка """
    return render(request, 'index.html', locals())


def prediction(request):
    """ Выбор предсказания для Ajax запроса по присланному номеру подарка """
    try:
        gift = int(request.POST.get('number_gift'))
    except:
        return redirect('index')
    print(gift, '------------------------------')
    return render(request, 'index.html', locals())