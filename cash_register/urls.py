from django.urls import path
from . import  views

urlpatterns = [
    path('', views.mainMenu, name='mainMenu'),
    path('scanItems/', views.scanItems, name='scanItems'),
    path('payment/', views.payment, name='payment'),
]