from django.contrib import admin
from .models import vam_productor, vam_asociacion_nacional

admin.site.site_header = "Gestión de Productores"

def custom_titled_filter(title):
    class Wrapper(admin.FieldListFilter):
        def __new__(cls, *args, **kwargs):
            instance = admin.FieldListFilter.create(*args, **kwargs)
            instance.title = title
            return instance
    return Wrapper
class ProductorAdmin(admin.ModelAdmin):
    list_display  =  ('id_productor', 'nombre', 'pag_web', 'email', 'id_asociacion'  )
    list_filter = [('id_productor',  custom_titled_filter('ID')),('nombre', custom_titled_filter('Nombre')), ('pag_web', custom_titled_filter('Página web')),( 'email', custom_titled_filter('Email')), ('id_asociacion__nombre', custom_titled_filter('Asociación')) ]
    search_fields = ['id_productor', 'nombre', 'pag_web',]
    list_per_page = 10
    def changelist_view(self, request, extra_context=None):
        extra_context = {'title': 'Ficha de Productores'}
        return super(ProductorAdmin, self).changelist_view(request, extra_context=extra_context)


admin.site.register(vam_productor, ProductorAdmin)