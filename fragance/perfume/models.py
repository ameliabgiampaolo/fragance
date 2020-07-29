from django.db import models

class vam_pais(models.Model):
    class Meta:
        db_table = 'vam_pais'

    id_pais = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=20)

class vam_asociacion_nacional(models.Model):
    class Meta:
        db_table = 'vam_asociacion_nacional'

    id_asociacion = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=15)
    region = models.CharField(max_length=15) #check = asia-pacifico, europa, norteamerica, latinoamerica
    id_pais = models.ForeignKey(vam_pais, on_delete=models.CASCADE, db_column='id_pais')

class vam_proveedor(models.Model):
    class Meta:
        db_table = 'vam_proveedor'

    id_proveedor = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=20)
    pag_web = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    id_pais = models.ForeignKey(vam_pais, on_delete=models.CASCADE, db_column='id_pais')
    id_asociacion = models.ForeignKey(vam_asociacion_nacional, on_delete=models.CASCADE, db_column='id_asociacion', null=True)

class vam_productor(models.Model):
    class Meta:
        db_table = 'vam_productor'

    id_productor = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=20)
    pag_web = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    id_asociacion = models.ForeignKey(vam_asociacion_nacional, on_delete=models.CASCADE, db_column='id_asociacion', null=True)

class vam_miembro_ifra(models.Model):
    class Meta:
        db_table = 'vam_miembro_ifra'
    
    id_miembro = models.IntegerField(primary_key=True)
    fecha_inicial = models.DateField()
    tipo = models.CharField(max_length=15, null=True) #check = principal, nacional, secundario
    fecha_final = models.DateField(null=True)
    id_proveedor = models.ForeignKey(vam_proveedor, on_delete=models.CASCADE, db_column='id_proveedor', null=True)
    id_productor = models.ForeignKey(vam_productor, on_delete=models.CASCADE, db_column='id_productor', null=True)

class vam_telefono(models.Model):
    class Meta:
        db_table = 'vam_telefono'

    id_telefono = models.IntegerField(primary_key=True)
    numero = models.BigIntegerField()
    tipo = models.CharField(max_length=15, null=True) #check = oficina, personal, fax
    id_proveedor = models.ForeignKey(vam_proveedor, on_delete=models.CASCADE, db_column='id_proveedor', null=True)
    id_productor = models.ForeignKey(vam_productor, on_delete=models.CASCADE, db_column='id_productor', null=True)

class vam_perfume(models.Model):
    class Meta:
        db_table = 'vam_perfume'

    id_perfume = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=300)
    genero = models.CharField(max_length=1) #check = f, m, u
    tipo_perfume = models.CharField(max_length=10) #check = por fases, monolitica
    edad_inspiracion = models.CharField(max_length=10) #check = adulto, juvenil, infantil, atemporal

class vam_ingrediente_esencia(models.Model):
    class Meta:
        db_table = 'vam_ingrediente_esencia'

    id_ingrediente_esencia = models.IntegerField(primary_key=True)
    tsca_cas_numeric = models.IntegerField()
    ipc_numeric = models.IntegerField(null=True)
    einecs_numeric = models.IntegerField(null=True) 
    descrip_proceso = models.CharField(max_length=300, null=True)
    descripcion_visual = models.CharField(max_length=300)
    parte_procesada = models.CharField(max_length=30, null=True)	
    fecha_caducidad = models.DateField(null=True)
    solubilidad = models.CharField(max_length=50, default='fail', null=True)
    inflamabilidad = models.IntegerField(null=True) 
    tipo_sustancia  = models.CharField(max_length=25) #'aceite-esencial','esencia-sintetica','disolvente-solido','disolvente-liquido','fijador'
    id_proveedor  = models.ForeignKey(vam_proveedor, on_delete=models.CASCADE, db_column='id_proveedor')
    nombre = models.CharField(max_length=30)

class vam_pais_prod(models.Model):
    class Meta:
        db_table = 'vam_pais_prod'

    id_productor = models.ForeignKey(vam_productor, on_delete=models.CASCADE, db_column='id_productor')
    id_pais = models.ForeignKey(vam_pais, on_delete=models.CASCADE, db_column='id_pais', default=1)

class vam_ingesen_origen(models.Model):
    class Meta:
        db_table = 'vam_ingesen_origen'

    id_ingrediente_esencia = models.ForeignKey(vam_ingrediente_esencia, on_delete=models.CASCADE, db_column='id_ingrediente_esencia')
    id_pais = models.ForeignKey(vam_pais, on_delete=models.CASCADE, db_column='id_pais')

class vam_ingrediente_otro(models.Model):
    class Meta:
        db_table = 'vam_ingrediente_otro'

    id_ingrediente_otro = models.IntegerField(primary_key=True)
    tsca_cas_numeric = models.IntegerField()
    ipc_numeric = models.IntegerField(null=True) 
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=300) 
    id_proveedor = models.ForeignKey(vam_proveedor, on_delete=models.CASCADE, db_column='id_proveedor')

class vam_ingotro_origen(models.Model):
    class Meta:
        db_table = 'vam_ingotro_origen'

    id_ingrediente_otro = models.ForeignKey(vam_ingrediente_otro, on_delete=models.CASCADE, db_column='id_ingrediente_otro')
    id_pais = models.ForeignKey(vam_pais, on_delete=models.CASCADE, db_column='id_pais')

class vam_ingrediente_prohibido(models.Model):
    class Meta:
        db_table = 'vam_ingrediente_prohibido'

    id_prohibido = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)

class vam_familia_olfativa(models.Model):
    class Meta:
        db_table = 'vam_familia_olfativa'
    
    id_familia = models.IntegerField(primary_key=True) 
    nombre = models.CharField(max_length=25)
    descripcion = models.CharField(max_length=300)

class vam_palabra_clave(models.Model):
    class Meta:
        db_table = 'vam_palabra_clave'

    id_palabra = models.IntegerField(primary_key=True)
    palabra = models.CharField(max_length=30)

class vam_fami_perf(models.Model):
    class Meta:
        db_table = 'vam_fami_perf'

    id_familia_olfativa = models.ForeignKey(vam_familia_olfativa, on_delete=models.CASCADE, db_column='id_familia_olfativa')
    id_perfume = models.ForeignKey(vam_perfume, on_delete=models.CASCADE, db_column='id_perfume')

class vam_fami_palab(models.Model):
    class Meta:
        db_table = 'vam_fami_palab'

    id_familia_olfativa = models.ForeignKey(vam_familia_olfativa, on_delete=models.CASCADE, db_column='id_familia_olfativa')
    id_palabra = models.ForeignKey(vam_palabra_clave, on_delete=models.CASCADE, db_column='id_palabra')

class vam_esencia_perfume(models.Model):
    class Meta:
        db_table = 'vam_esencia_perfume'

    id_esencia_perfume = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    tipo = models.CharField(max_length=10) #check = natural, sintetico
    descripcion = models.CharField(max_length=300)

class vam_fami_esenperf(models.Model):
    class Meta:
        db_table = 'vam_fami_esenperf'

    id_familia_olfativa = models.ForeignKey(vam_familia_olfativa, on_delete=models.CASCADE, db_column='id_familia_olfativa')
    id_esencia_perfume = models.ForeignKey(vam_esencia_perfume, on_delete=models.CASCADE, db_column='id_esencia_perfume')

class vam_componente(models.Model):
    class Meta:
        db_table = 'vam_componente'

    id_componente = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=25)
    descripcion = models.CharField(max_length=300)

class vam_ingotro_comp(models.Model):
    class Meta:
        db_table = 'vam_ingotro_comp'

    id_ingrediente_otro = models.ForeignKey(vam_ingrediente_otro, on_delete=models.CASCADE, db_column='id_ingrediente_otro')
    id_componente = models.ForeignKey(vam_componente, on_delete=models.CASCADE, db_column='id_componente')

class vam_perf_comp(models.Model):
    class Meta:
        db_table = 'vam_perf_comp'

    id_perfume = models.ForeignKey(vam_perfume, on_delete=models.CASCADE, db_column='id_perfume')
    id_componente = models.ForeignKey(vam_componente, on_delete=models.CASCADE, db_column='id_componente')

class vam_perf_prod(models.Model):
    class Meta:
        db_table = 'vam_perf_prod'

    id_perfume = models.ForeignKey(vam_perfume, on_delete=models.CASCADE, db_column='id_perfume')
    id_productor = models.ForeignKey(vam_productor, on_delete=models.CASCADE, db_column='id_productor')

class vam_monolitico(models.Model):
    class Meta:
        db_table = 'vam_monolitico'

    id_perfume = models.ForeignKey(vam_perfume, on_delete=models.CASCADE, db_column='id_perfume', null=True)
    id_esencia_perfume = models.ForeignKey(vam_componente, on_delete=models.CASCADE, db_column='id_esencia_perfume')

class vam_fami_ingesen(models.Model):
    class Meta:
        db_table = 'vam_fami_ingesen'

    id_familia_olfativa = models.ForeignKey(vam_familia_olfativa, on_delete=models.CASCADE, db_column='id_familia_olfativa')    
    id_ingrediente_esencia = models.ForeignKey(vam_ingrediente_esencia, on_delete=models.CASCADE, db_column='id_ingrediente_esencia')

class vam_fami_ingotro(models.Model):
    class Meta:
        db_table = 'vam_fami_ingotro'

    id_familia_olfativa = models.ForeignKey(vam_familia_olfativa, on_delete=models.CASCADE, db_column='id_familia_olfativa')    
    id_ingrediente_otro = models.ForeignKey(vam_ingrediente_esencia, on_delete=models.CASCADE, db_column='id_ingrediente_otro')

class vam_fase(models.Model):
    class Meta:
        db_table = 'vam_fase'

    id_fase = models.IntegerField(primary_key=True)
    id_esencia_perfume = models.ForeignKey(vam_esencia_perfume, on_delete=models.CASCADE)
    id_perfume = models.ForeignKey(vam_perfume, on_delete=models.CASCADE, db_column='id_perfume')
    tipo_fases = models.CharField(max_length=7) #check = 'notas-salida','notas-corazon','notas-fondo'

class vam_intensidad(models.Model):
    class Meta:
        db_table = 'vam_intensidad'

    id_perfume = models.ForeignKey(vam_perfume, on_delete=models.CASCADE, db_column='id_perfume')
    id_intensidad = models.IntegerField(primary_key=True)
    tipo = models.CharField(max_length=3) #check = 'p','edp','edt','edc','eds'
    concentracion = models.IntegerField()
    descripcion = models.CharField(max_length=300, null=True)

class vam_presentacion_perfume(models.Model):
    class Meta:
        db_table = 'vam_presentacion_perfume'

    id_presentacion_perfume = models.IntegerField(primary_key=True)
    id_perfume = models.ForeignKey(vam_perfume, on_delete=models.CASCADE, db_column='id_perfume')
    id_intensidad = models.ForeignKey(vam_intensidad, on_delete=models.CASCADE, db_column='id_intensidad')
    volumen = models.IntegerField()

class vam_perfumista(models.Model):
    class Meta:
        db_table = 'vam_perfumista'

    id_perfumista = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    segundo_apellido = models.CharField(max_length=20)
    genero = models.CharField(max_length=1)
    id_productor = models.ForeignKey(vam_productor, on_delete=models.CASCADE, db_column='id_productor')
    id_pais = models.ForeignKey(vam_pais, on_delete=models.CASCADE, db_column='id_pais')
    segundo_nombre = models.CharField(max_length=20, null=True)

class vam_perf_perfumist(models.Model):
    class Meta:
        db_table = 'vam_perf_perfumist'

    id_perfume = models.ForeignKey(vam_perfume, on_delete=models.CASCADE, db_column='id_perfume')
    id_perfumista = models.ForeignKey(vam_perfumista, on_delete=models.CASCADE, db_column='id_perfumista')

class vam_presentacion(models.Model):
    class Meta:
        db_table = 'vam_presentacion'

    id_presentacion = models.IntegerField(primary_key=True)
    volumen = models.FloatField()
    precio = models.FloatField()
    id_ingrediente_esencia = models.ForeignKey(vam_ingrediente_esencia, on_delete=models.CASCADE, db_column='id_ingrediente_esencia', null=True)
    id_ingrediente_otro = models.ForeignKey(vam_ingrediente_otro, on_delete=models.CASCADE, db_column='id_ingrediente_otro', null=True)

class vam_ingesen_comp(models.Model):
    class Meta:
        db_table = 'vam_ingesen_comp'

    id_ingrediente_esencia = models.ForeignKey(vam_ingrediente_esencia, on_delete=models.CASCADE, db_column='id_ingrediente_esencia')
    id_componente = models.ForeignKey(vam_componente, on_delete=models.CASCADE, db_column='id_componente')

class vam_variable(models.Model):
    class Meta:
        db_table = 'vam_variable'

    id_variable = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=25)
    descripcion = models.CharField(max_length=300)

class vam_evaluacion_criterio(models.Model):
    class Meta:
        db_table = 'vam_evaluacion_criterio'

    id_productor = models.ForeignKey(vam_productor, on_delete=models.CASCADE, db_column='id_productor')
    id_variable = models.ForeignKey(vam_variable, on_delete=models.CASCADE, db_column='id_variable')
    fecha_inicio = models.DateField()
    peso = models.IntegerField()
    tipopor = models.CharField(max_length=30)
    fecha_fin = models.DateField(null=True)

class vam_escala_valorada(models.Model):
    class Meta:
        db_table = 'vam_escala_valorada'

    id_productor = models.ForeignKey(vam_productor, on_delete=models.CASCADE, db_column='id_productor')
    id_escala = models.IntegerField(primary_key=True)
    fecha_inicio = models.DateField()
    rango_inicio = models.IntegerField()
    rango_fin = models.IntegerField(null=True)
    fecha_final = models.DateField(null=True)

class vam_resultado_evaluacion(models.Model):
    class Meta:
        db_table = 'vam_resultado_evaluacion'

    id_productor = models.ForeignKey(vam_productor, on_delete=models.CASCADE, db_column='id_productor')
    id_proveedor = models.ForeignKey(vam_proveedor, on_delete=models.CASCADE, db_column='id_proveedor')
    fecha = models.DateField()
    resultado = models.IntegerField()
    tipoeva = models.CharField(max_length=7)

class vam_contrato(models.Model):
    class Meta:
        db_table = 'vam_contrato'

    id_contrato = models.IntegerField(primary_key=True)
    fecha_inicio = models.DateField()
    exclusividad = models.CharField(max_length=30)
    id_productor = models.ForeignKey(vam_productor, on_delete=models.CASCADE, db_column='id_productor')
    id_proveedor = models.ForeignKey(vam_proveedor, on_delete=models.CASCADE, db_column='id_proveedor')
    motivo_cancelado = models.CharField(max_length=300, null=True)
    fecha_cancelado = models.DateField(null=True)
    quien_cancela = models.CharField(max_length=30, null=True)

class vam_elemento_contrato(models.Model):
    class Meta:
        db_table = 'vam_elemento_contrato'

    id_contrato = models.ForeignKey(vam_contrato, on_delete=models.CASCADE, db_column='id_contrato')
    id_elemento_contrato = models.IntegerField(primary_key=True)
    id_ingrediente_esencia = models.ForeignKey(vam_ingrediente_esencia, on_delete=models.CASCADE, db_column='id_ingrediente_esencia', null=True)
    id_ingrediente_otro = models.ForeignKey(vam_ingrediente_otro, on_delete=models.CASCADE, db_column='id_ingrediente_otro', null=True)

class vam_renovacion(models.Model):
    class Meta:
        db_table = 'vam_renovacion'

    id_contrato = models.ForeignKey(vam_contrato, on_delete=models.CASCADE, db_column='id_contrato')
    id_renovacion = models.IntegerField(primary_key=True)
    fecha = models.DateField()

class vam_condicion_envio(models.Model):
    class Meta:
        db_table = 'vam_condicion_envio'

    id_proveedor = models.ForeignKey(vam_proveedor, on_delete=models.CASCADE, db_column='id_proveedor')
    id_pais = models.ForeignKey(vam_pais, on_delete=models.CASCADE, db_column='id_pais')
    id_condicion_envio = models.IntegerField(primary_key=True)
    medio_transporte = models.CharField(max_length=15)
    descripcion = models.CharField(max_length=300)
    costo = models.IntegerField()

class vam_condicion_pago(models.Model):
    class Meta:
        db_table = 'vam_condicion_pago'

    id_proveedor = models.ForeignKey(vam_proveedor, on_delete=models.CASCADE, db_column='id_proveedor')
    id_condicion_pago = models.IntegerField(primary_key=True)
    tipo_condicion = models.CharField(max_length=250)
    descripcion = models.CharField(max_length=300, null=True)
    cuotas = models.IntegerField(null=True)
    porcen_cuota = models.IntegerField(null=True)
    meses_cuotas = models.IntegerField(null=True)

class vam_condicion_contrato(models.Model):
    class Meta:
        db_table = 'vam_condicion_contrato'

    id_contrato = models.ForeignKey(vam_contrato, on_delete=models.CASCADE, db_column='id_contrato')
    id_condicion_contrato = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=300)
    id_condicion_pago = models.ForeignKey(vam_condicion_pago, on_delete=models.CASCADE, db_column='id_condicion_pago', null=True)
    id_proveedor_pago = models.IntegerField(null=True)
    id_proveedor_envio = models.IntegerField(null=True)
    id_condicion_envio = models.ForeignKey(vam_condicion_envio, on_delete=models.CASCADE, db_column='id_condicion_envio', null=True)
    id_pais_envio = models.IntegerField(null=True)

class vam_pedido(models.Model):
    class Meta:
        db_table = 'vam_pedido'

    id_pedido = models.IntegerField(primary_key=True)
    estatus = models.CharField(max_length=10)
    descripcion = models.CharField(max_length=10)
    fecha_emision = models.DateField()
    id_productor = models.ForeignKey(vam_productor, on_delete=models.CASCADE, db_column='id_productor')
    id_proveedor = models.ForeignKey(vam_proveedor, on_delete=models.CASCADE, db_column='id_proveedor')
    nfactura = models.IntegerField()
    precio_total = models.FloatField()
    id_condicion_envio = models.ForeignKey(vam_condicion_envio, on_delete=models.CASCADE, db_column='id_condicion_envio', null=True)
    id_contrato_envio = models.IntegerField(null=True)
    id_condicion_pago = models.ForeignKey(vam_condicion_pago, on_delete=models.CASCADE, db_column='id_condicion_pago', null=True)
    id_contrato_pago = models.IntegerField(null=True)

class vam_detalle_pedido(models.Model):
    class Meta:
        db_table = 'vam_detalle_pedido'

    id_pedido = models.ForeignKey(vam_pedido, on_delete=models.CASCADE, db_column='id_pedido')
    id_detalle = models.IntegerField(primary_key=True)
    cantidad = models.IntegerField()
    subtotal = models.FloatField()
    id_presentacion = models.ForeignKey(vam_presentacion_perfume, on_delete=models.CASCADE, db_column='id_presentacion')

class vam_pago(models.Model):
    class Meta:
        db_table = 'vam_pago'

    id_pedido = models.ForeignKey(vam_pedido, on_delete=models.CASCADE, db_column='id_pedido')
    id_pago = models.IntegerField(primary_key=True)
    fecha_pago = models.DateField()
    monto_pagado = models.IntegerField()