from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'receitas/home.html', {
        'name': "randolfo"
    }) 

    
def contato(request):
    return HttpResponse('contato')


def sobre(request):
    return HttpResponse('sobre')
