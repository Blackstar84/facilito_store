from django.urls import path
from . import views
from products.views import ProductDetailView

app_name = 'products'

urlpatterns = [
    path('search',views.ProductSearchListView.as_view(), name='search' ),
    path('<slug:slug>', views.ProductDetailView.as_view(), name='product'),
    
]