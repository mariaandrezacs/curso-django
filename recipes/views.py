from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'name': 'Luiz Otávio',
    })

def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={
        'name': 'Luiz Otávio',
    })


'''def sobre(request):
    return render(request, 'temp/temp.html')
def sobre(request):
    return render(request, 'recipes/sobre.html')


def contato(request):
    return HttpResponse('CONTATO')'''