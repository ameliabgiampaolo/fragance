from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .forms import ProductorForm, ProveedorForm
from .models import vam_contrato, vam_elemento_contrato, vam_productor, vam_proveedor, vam_ingrediente_esencia, vam_ingrediente_otro, vam_pedido, vam_pago
import datetime

def index(request):
    context = {} 
    return render(request, 'perfume/index.html', context)

def next_val(model):
    tabla = model.objects.all()
    return len(tabla) + 1

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

    elemento = vam_elemento_contrato.objects.filter(id_contrato=contrato).values('id_ingrediente_esencia_id', 'id_ingrediente_otro_id')
    otro = None

    for e in elemento:
        esencia = vam_ingrediente_esencia.objects.get(id_ingrediente_esencia = e['id_ingrediente_esencia_id'])
        if e['id_ingrediente_otro_id'] != None:
            esencia_otro = vam_ingrediente_otro.objects.get(id_ingrediente_otro = e['id_ingrediente_otro_id'])
            otro = True
        
    if otro:
        context = {'contrato': contrato, 'elemento': elemento, 'esencia': esencia, 'esencia_otro': esencia_otro}
    else:
        context = {'contrato': contrato, 'elemento': elemento, 'esencia': esencia}
    return render(request, 'perfume/compra.html', context)

def pago(request):
    pedido = vam_pedido.objects.filter(estatus='pendiente')
    now = datetime.date.today()
    
    context = {'pedido': pedido}
    return render(request, 'perfume/pago.html', context)

def save(request, id_pedido):
    pedido = vam_pedido.objects.get(id_pedido=id_pedido)
    now = datetime.date.today()

    pago = vam_pago()
    pago.id_pago = next_val(vam_pago)
    pago.fecha_pago = now
    pago.monto_pagado = pedido.precio_total
    pago.id_pedido = pedido
    pedido.estatus = 'procesado'
    pago.save()
    pedido.save()

    pedido = vam_pedido.objects.filter(estatus='pendiente')
    
    context = {'pedido': pedido}
    return render(request, 'perfume/pago.html', context)