from django import forms

from .models import vam_productor, vam_proveedor

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



