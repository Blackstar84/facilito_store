from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # return HttpResponse('Hola mundo!')
    return render(request, 'index.html' , {
        'message': 'Nuevo mensaje desde la vista',
        'suma': 10 + 20,
        'booleano': True,
        'lista': [1,2,3,4],
        'title': 'Título'
    })