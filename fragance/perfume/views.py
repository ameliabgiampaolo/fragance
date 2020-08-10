from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
import datetime
from .models import vam_contrato, vam_presentacion, vam_condicion_envio, vam_detalle_pedido, vam_elemento_contrato, vam_productor, vam_proveedor, vam_ingrediente_esencia, vam_ingrediente_otro, vam_pedido, vam_pago, vam_condicion_pago
from django.forms import formset_factory
import random
from .forms import ProductorForm, ProveedorForm, CompraForm, IngForm, CantidadForm

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
    productor = id_productor
    proveedor = id_proveedor
    condicion_envio = vam_condicion_envio.objects.get(id_condicion_envio = 9)
    condicion_pago = vam_condicion_pago.objects.get(id_condicion_pago = 2)
    try:
        contrato = vam_contrato.objects.get(id_productor=id_productor, id_proveedor=id_proveedor)
    except vam_contrato.DoesNotExist:
        context = {}
        return render(request, 'perfume/error404.html', context)

    elemento = vam_elemento_contrato.objects.filter(id_contrato=contrato).values('id_ingrediente_esencia_id', 'id_ingrediente_otro_id')
    ingredientes = []
    for e in elemento:
        if e['id_ingrediente_esencia_id'] != None:
            ingredientes.append(vam_ingrediente_esencia.objects.get(id_ingrediente_esencia = e['id_ingrediente_esencia_id']).nombre)
        else:
            ingredientes.append(vam_ingrediente_otro.objects.get(id_ingrediente_otro = e['id_ingrediente_otro_id']).nombre) 

    CantidadFormset = formset_factory(CantidadForm, extra=len(ingredientes))

    if request.method == 'POST':
        form = IngForm(ingredientes, request.POST)
        formset = CantidadFormset(request.POST)
        cantidad = []
        resumen_ingrediente = ''
        resumen_cantidad = ''
        now = datetime.date.today()
        pedido_creado = False
        i = 0
        if formset.is_valid():

            for fset in formset:
                if fset.cleaned_data.get('cantidad') != None:
                    ingrediente = ingredientes[i]
                    resumen_ingrediente += ingrediente + ','
                    cantidad = fset.cleaned_data.get('cantidad')
                    resumen_cantidad += str(cantidad) + ','
                    esencia = True
                    try:
                        ingrediente2 = vam_ingrediente_esencia.objects.get(nombre=ingrediente)
                    except vam_ingrediente_esencia.DoesNotExist as e:
                        ingrediente2 = vam_ingrediente_otro.objects.get(nombre=ingrediente)
                        esencia = False
                        
                    if esencia == True:
                        presentacion = vam_presentacion.objects.filter(id_ingrediente_esencia=ingrediente2)[0]
                    else:
                        presentacion = vam_presentacion.objects.filter(id_ingrediente_otro=ingrediente2)[0]

                    productor_id = vam_productor.objects.get(id_productor=id_productor)
                    proveedor_id = vam_proveedor.objects.get(id_proveedor=id_proveedor)

                    if pedido_creado == False:
                        id_pedido = next_val(vam_pedido)
                        pedido = vam_pedido.objects.create_pedido(id_pedido,'pendiente', 'via email', now, productor_id, proveedor_id, random.randint(1,100), presentacion.precio, condicion_envio, 1, condicion_pago)
                        pedido_creado = True
                        
                    id_detalle = next_val(vam_detalle_pedido)
                    detalle = vam_detalle_pedido.objects.create_detalle(id_detalle,pedido, cantidad, presentacion.precio, presentacion)
                    id_pago = next_val(vam_pago)
                    pago = vam_pago.objects.create_pago(id_pago, now, presentacion.precio, pedido)
                    i += 1
                
            return redirect('resumen', id_pedido, resumen_cantidad, proveedor, productor, resumen_ingrediente)
    else:  
        formset = CantidadFormset()
        form = IngForm(ingredientes)
        context = {'ingredientes': ingredientes, 'form': form, 'formset': formset }
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

def separar(ingredientes):
    palabra = ''
    lista = []
    for i in range(len(ingredientes)):
        if ingredientes[i] != ',':
            palabra += ingredientes[i]
        else:
            lista.append(palabra)
            palabra = ''

    return lista

def intercalar(lista, lista2):
    intercalado = []
    cant = False
    j = 0
    for i in range(len(lista)):
        intercalado.append(list(lista[i] + lista2[i]))
    return intercalado

def resumen(request, id_pedido, cantidad, proveedor, productor, ingredientes):
    ingredientes = separar(ingredientes)
    cantidad = separar(cantidad)
    proveedor = vam_proveedor.objects.get(id_proveedor=proveedor)
    productor = vam_productor.objects.get(id_productor=productor)
   # ingredientes = intercalar(ingredientes, cantidad)
    context = {'id_pedido': id_pedido, 'cantidad': cantidad, 'proveedor': proveedor, 'productor': productor, 'ingredientes': ingredientes}
    return render(request, 'perfume/resumen.html', context)


def delete(request, id_pedido): 
    context ={} 
    detalle_pedido = vam_detalle_pedido.objects.filter(id_pedido=id_pedido)
    pedido = vam_pedido.objects.filter(id_pedido=id_pedido)

    detalle_pedido.delete()
    pedido.delete()  
    return render(request, 'perfume/index.html', context)