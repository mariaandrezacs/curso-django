from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, 'recipes/home.html')


'''def sobre(request):
    return render(request, 'temp/temp.html')
def sobre(request):
    return render(request, 'recipes/sobre.html')


def contato(request):
    return HttpResponse('CONTATO')'''