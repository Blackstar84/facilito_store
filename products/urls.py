from django.urls import path
from . import views
from products.views import ProductDetailView

urlpatterns = [
    path('<slug:slug>', views.ProductDetailView.as_view(), name='product'),
]