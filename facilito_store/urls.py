from django.contrib import admin
from django.urls import path

from products.views import ProductListView
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ProductListView.as_view(), name='index'),
    path('usuarios/login', views.login_view, name='login'),
    path('usuarios/logout', views.logout_view, name='logout'),
    path('usuarios/registro', views.register, name='register'),
]
