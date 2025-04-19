from django.urls import path
from frontend.views import calculadora

urlpatterns = [
    path('',  calculadora, name='home')
]