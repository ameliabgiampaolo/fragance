from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .forms import ProductorForm, ProveedorForm
from .models import vam_contrato, vam_elemento_contrato, vam_productor, vam_proveedor, vam_ingrediente_esencia, vam_ingrediente_otro

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
    contrato = vam_contrato.objects.get(id_productor=id_productor, id_proveedor=id_proveedor)

    elemento = vam_elemento_contrato.objects.filter(id_contrato=contrato).values('id_ingrediente_esencia_id')

    for e in elemento:
        esencia = vam_ingrediente_esencia.objects.get(id_ingrediente_esencia = e['id_ingrediente_esencia_id'])

    

    context = {'contrato': contrato, 'elemento': elemento, 'esencia': esencia}
    return render(request, 'perfume/compra.html', context)

def pedido(request, esencia_id):
    pass