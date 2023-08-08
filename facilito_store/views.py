from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout


def index(request):
    # return HttpResponse('Hola mundo!')
    return render(request, 'index.html' , {
        'message': 'Listado de productos',        
        'title': 'Productos',
        'products': [
            {'title' : 'Playera', 'price': 5, 'stock': True}, # producto
            {'title' : 'Camisa', 'price': 7, 'stock': True},
            {'title' : 'Mochila', 'price': 20, 'stock': False},
        ]
    })
    
    
def login_view(request):
    # print(request.method)
    if request.method == 'POST':
        username = request.POST.get('username') #Diccionario
        password = request.POST.get('password') #Diccionario
        
        user =authenticate(username=username, password = password)
        
        if user:
            login(request, user)
            print("Usuario Autenticado")
        else:
            print("Usuario no Autenticado")
        
    return render(request, 'users/login.html', {})

   