from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('seleccion', views.seleccion, name='seleccion'),
    path('compra/<int:id_productor>/<int:id_proveedor>', views.compra, name='compra'),
    path('error404', views.compra, name='error404'),
    path('resumen/<int:id_pedido>/<int:cantidad>/<int:proveedor>/<int:productor>/(<str:ingrediente>', views.resumen, name='resumen'),
    path('pago', views.pago, name='pago'),
    path('delete/<int:id_pedido>', views.delete, name='delete'),
    path('save/<int:id_pedido>', views.save, name='save'),
]