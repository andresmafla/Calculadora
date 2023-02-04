from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1>Hola, mundo. Estás en la página de inicio de tu app llamada calculadora.</h1>")

def sumar(request,op1,op2):
    return HttpResponse(op1+op2)

def restar(request,op1,op2):
    return HttpResponse(op1-op2)

def multi(request,op1,op2):
    return HttpResponse(op1*op2)

def div(request,op1,op2):
    try:
        result = op1/op2
    except ZeroDivisionError:
        result = "No division by zero allowed!"
    return HttpResponse(result)