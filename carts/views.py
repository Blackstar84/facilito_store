from django.shortcuts import render

# Create your views here.

def cart(request):
    # Crear una session
    # request.session['cart_id'] = '123' # Diccionario
    
    # Obtenemos el valor de una session
    valor = request.session.get('cart_id')
    
    
    # Eliminar una session
    request.session['cart_id'] = None
    
    return render(request, 'carts/cart.html', {})

