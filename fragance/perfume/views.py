from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .forms import ProductorForm, ProveedorForm

def index(request):
    context = {} 
    return render(request, 'perfume/index.html', context)

def seleccion(request):
    form = ProductorForm()
    form2 = ProveedorForm()
    return render(request, 'perfume/seleccion.html', { 'form': form,'form2': form2  })