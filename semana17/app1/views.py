from django.shortcuts import render
from .models import *
from .templates import *

def list_clien(request):
    Clientes = Cliente.objects.all()
    return render(request,'Clientes.html',{'clientes':Clientes})

# views.py
def list_are(request):
    Areas = Area.objects.all()
    return render(request, 'Areas.html', {'areas': Areas})


def list_empl(request):
    Empleados = Empleado.objects.all()
    return render(request, 'Empleados.html',{'empleados':Empleados})


def lis_ven(request):
    Ventas = Venta.objects.all()
    return render(request,'Ventas.html',{'ventas':Ventas})
