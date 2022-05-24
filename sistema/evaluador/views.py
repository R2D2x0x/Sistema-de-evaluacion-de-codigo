from django.shortcuts import redirect, render

# Create your views here.

def autenticacion(request):
    return render(request, "autenticacion.html")

def crear_ejercicios(request):
    return render(request, "crear_ejercicios.html")