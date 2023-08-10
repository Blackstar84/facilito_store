from django.urls import path
from . import views
from products.views import ProductDetailView

urlpatterns = [
    path('<pk>', views.ProductDetailView.as_view(), name='product'),
]