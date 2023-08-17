from django.contrib import admin
from django.urls import path
from django.urls import include
from products.views import ProductListView
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ProductListView.as_view(), name='index'),
    path('usuarios/login', views.login_view, name='login'),
    path('usuarios/logout', views.logout_view, name='logout'),
    path('usuarios/registro', views.register, name='register'),
    path('productos/', include('products.urls')),
    path('carrito/', include('carts.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)