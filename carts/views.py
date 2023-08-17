from django.shortcuts import render
from .models import Cart


# Create your views here.

def cart(request):
    # request.session['cart_id'] = None
    # Con esto obtenemos el usuario autenticado
    user = request.user if request.user.is_authenticated else None
    cart_id = request.session.get('cart_id')
    
    if cart_id:
        cart = Cart.objects.get(cart_id=cart_id) # Obtenemos el carrito de la base de datos
    else:
        cart = Cart.objects.create(user=user) # Creamos un nuevo carrito
        
    request.session['cart_id'] = cart.cart_id   
    
    return render(request, 'carts/cart.html', {})

