from django import forms

from .models import vam_productor, vam_proveedor, vam_ingrediente_esencia, vam_ingrediente_otro

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

class IngForm(forms.Form):
  def __init__(self, choice, *args, **kwargs):
    super(IngForm, self).__init__(*args, *kwargs)
    self.fields['ingredientes'] = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=tuple([(name, name) for name in choice]))
    #self.fields['cantidad'] = forms.Field(widget=forms.NumberInput(attrs= { 'class': 'form-control', 'style': 'width: 100px; text-align: center; '}))
  class Meta:
    fields = ('ingredientes',)

class CantidadForm(forms.Form):
  cantidad = forms.Field(widget=forms.NumberInput(attrs= { 'class': 'form-control', 'style': 'width: 100px; text-align: center; '}))