from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('sumar/<int:op1>/<int:op2>', views.sumar),
    path('restar/<int:op1>/<int:op2>', views.restar),
    path('multiplicar/<int:op1>/<int:op>', views.multi),
    path('dividir/<int:op1>/<int:op2>', views.div),
]