from django.shortcuts import render
from .utils import get_or_create_order, breadcrumb, destroy_order
from carts.utils import destroy_cart
from carts.utils import get_or_create_cart
from .models import Order
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from shipping_addresses.models import ShippingAddress
from django.contrib import messages

from django.core.mail import send_mail

from .mails import Mail

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView


# Create your views here.


class OrderListView(LoginRequiredMixin, ListView):
   login_url = 'login'
   template_name = 'orders/order.html'




@login_required(login_url='login')
def order(request):
    cart = get_or_create_cart(request) 
    order = get_or_create_order(cart, request)
    return render(request, 'orders/order.html', {
       'cart': cart,
       'order': order,
       'breadcrumb': breadcrumb(),
    })
    
@login_required(login_url='login')    
def address(request):
   cart = get_or_create_cart(request)
   order = get_or_create_order(cart, request)
   shipping_address = order.get_or_set_shipping_address()
   can_choose_address = request.user.shippingaddress_set.count() > 1
   
   return render(request, 'orders/address.html',{
      'cart': cart,
      'order': order,
      'shipping_address': shipping_address,
      'can_choose_address': can_choose_address,
      'breadcrumb': breadcrumb(address=True)
   })
   
   
@login_required(login_url='login')     
def select_address(request):
      shipping_addresses = request.user.shippingaddress_set.all()
      
      return render(request, 'orders/select_address.html', {
         'breadcrumb': breadcrumb(address=True),
         'shipping_addresses': shipping_addresses
      })
   
@login_required(login_url='login')    
def check_address(request, pk):
   cart = get_or_create_cart(request)
   order = get_or_create_order(cart, request)
   
   shipping_address = get_object_or_404(ShippingAddress, pk=pk)
   
   if request.user.id != shipping_address.user_id:
      return redirect('carts:cart')
   
   order.update_shipping_address(shipping_address)
   
   return redirect('orders:address')
   
   
@login_required(login_url='login')
def confirm(request):
   cart = get_or_create_cart(request)
   order = get_or_create_order(cart,request)
   
   shipping_address = order.shipping_address
   
   if shipping_address is None:
      return redirect('orders:address')
   
   return render(request, 'orders/confirm.html',{
      'cart': cart,
      'order': order,
      'breadcrumb': breadcrumb(address=True, confirmation=True),
      'shipping_address': shipping_address
   })
   
   
@login_required(login_url='login')
def cancel(request):
   cart = get_or_create_cart(request)
   order = get_or_create_order(cart,request) 
   
   if request.user.id != order.user_id:
      return redirect('carts:cart')
   
   order.cancel()
   
   destroy_cart(request)
   destroy_order(request)
   
   
   messages.error(request, 'Orden cancelada')
   
   return redirect('index')

   
@login_required(login_url='login')
def complete(request):
   cart = get_or_create_cart(request)
   order = get_or_create_order(cart,request)
   
   if request.user.id != order.user_id:
     return redirect('carts:cart')
  
   order.complete()
   # Esto ya no funciona con gmail por su protocolo de seguridad
   # Mail.send_complete_order(order,request.user)
  
   destroy_cart(request)
   destroy_order(request)
   
   messages.success(request, 'Compra completada exitosamente')
   return redirect('index')