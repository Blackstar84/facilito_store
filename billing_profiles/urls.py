from django.urls import path

from . import views

app_name = 'billing_profiles'

urlpatterns = [
     path('', views.create, name='create'),
]

