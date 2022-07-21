from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.


def home(request):
    return render(request, 'receitas/home.html', context={
        'name': 'randolfo carvalhoo'
    })


def contato(request):
    return HttpResponse('contato12')


def sobre(request):
    return HttpResponse('sobre')


