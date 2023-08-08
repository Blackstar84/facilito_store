from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User

from .forms import RegisterForm


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
        
        user = authenticate(username=username, password = password)
        
        if user:
            login(request, user)
            messages.success(request,'Bienvenido {}'.format(user.username))
            return redirect('index')
        else:
            messages.error(request, 'Usuario o contraseña no válidos')
        
        
    return render(request, 'users/login.html', {})

def logout_view(request):
    logout(request)  
    messages.success(request, 'Sesión cerrada exitosamente')
    return redirect('login')

def register(request):
    form = RegisterForm(request.POST or None)
    if request.POST and form.is_valid():
        username = form.cleaned_data.get('username') # Diccionario
        email = form.cleaned_data.get('email') # Diccionario
        password = form.cleaned_data.get('password') # Diccionario
        # print(username)
        # print(email)
        # print(password)
        
        user = User.objects.create_user(username, email, password)
        if user:
            login(request, user)
            messages.success(request, 'Usuario creado exitosamente!!!')
            return redirect('index')
        
    return render(request, 'users/register.html', {
        'form': form
    })