from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # return HttpResponse('Hola mundo!')
    return render(request, 'index.html' , {
        #context
    })