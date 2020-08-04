from django import forms

from .models import vam_productor, vam_proveedor, vam_ingrediente_esencia

class ProductorForm(forms.ModelForm):

  productor = forms.ChoiceField(choices=[(pro.id_productor, pro.nombre) for pro in vam_productor.objects.all()])
  
  class Meta:
      model = vam_productor
      fields = ('productor', )

class ProveedorForm(forms.ModelForm):

  proveedor = forms.ChoiceField(choices=[(pro.id_proveedor, pro.nombre) for pro in vam_proveedor.objects.all()])
  
  class Meta:
      model = vam_proveedor
      fields = ('proveedor', )

class CompraForm(forms.Form):
  esencia = forms.CharField(label='Ingrediente', widget= forms.TextInput(attrs= { 'class': 'form-control', 'style': 'width: 300px; text-align: center; '}))
  cantidad = forms.Field(widget=forms.NumberInput(attrs= { 'class': 'form-control', 'style': 'width: 100px; text-align: center; '}))

class Ingrediente_esencia(forms.ModelForm):
  esencia = forms.ChoiceField(choices=[(ing.id_ingrediente_esencia, ing.nombre) for ing in vam_ingrediente_esencia.objects.all()])
  class Meta:
    model = vam_ingrediente_esencia
    fields = ('nombre',)

