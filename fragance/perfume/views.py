from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .forms import ProductorForm, ProveedorForm

def index(request):
    context = {} 
    return render(request, 'perfume/index.html', context)

def seleccion(request):
    if request.method == 'POST':
        form = ProductorForm(request.POST)
        form2 = ProveedorForm(request.POST)
        if form.is_valid() and form2.is_valid():
            id_productor = form.cleaned_data.get('productor')
            id_proveedor = form2.cleaned_data.get('proveedor')
            return redirect('compra', id_productor, id_proveedor)
    else:
        form = ProductorForm()
        form2 = ProveedorForm

    return render(request, 'perfume/seleccion.html', { 'form': form,'form2': form2  })

def compra(request, id_productor, id_proveedor):
    context = {}
    return render(request, 'perfume/index.html', context)