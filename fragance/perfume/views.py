from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
import datetime
from .models import vam_contrato, vam_presentacion, vam_detalle_ pedido, vam_elemento_contrato, vam_productor, vam_proveedor, vam_ingrediente_esencia, vam_ingrediente_otro, vam_pedido, vam_pago
from django.forms import formset_factory
import random
from .forms import ProductorForm, ProveedorForm, CompraForm

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
    ingredientes = []
    CompraFormset = formset_factory(CompraForm, extra=len(elemento))
    now = datetime.date.today()
    if request.method == 'POST':
        formset = CompraFormset(request.POST)
        if formset.is_valid():
            for form in formset:
                ingrediente = form.cleaned_data.get('esencia')
                cantidad = form.cleaned_data.get('cantidad')

                ingrediente2= vam_ingrediente_esencia.objects.get(nombre=ingrediente)
                if ingrediente2 == None:
                    ingrediente2= vam_ingrediente_otro.objects.get(nombre=ingrediente)

                presentacion = vam_presentacion.objects.filter(id_ingrediente_esencia=ingrediente2)[0]
                if presentacion == None:
                    presentacion = vam_presentacion.objects.filter(id_ingrediente_otro=ingrediente2)[0]

                id_productor = vam_productor.objects.get(id_productor=id_productor)
                id_proveedor = vam_proveedor.objects.get(id_proveedor=id_proveedor)
                id_pedido = next_val(vam_pedido)
                id_detalle = next_val(vam_detalle_pedido)
                pedido = vam_pedido.objects.create_pedido(id_pedido,'pendiente', 'nada', now, id_productor, id_proveedor, random.randint(1,100), presentacion.precio)
                detalle = vam_detalle_pedido.objects.create_detalle(id_detalle,pedido, cantidad, presentacion.precio, presentacion)
                
            return redirect('index')

    else:
        formset = CompraFormset
        for e in elemento:
            if e['id_ingrediente_esencia_id'] != None:
                ingredientes.append(vam_ingrediente_esencia.objects.get(id_ingrediente_esencia = e['id_ingrediente_esencia_id']).nombre)
            else:
                ingredientes.append(vam_ingrediente_otro.objects.get(id_ingrediente_otro = e['id_ingrediente_otro_id']).nombre) 

        context = {'ingredientes': ingredientes, 'formset': formset }
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