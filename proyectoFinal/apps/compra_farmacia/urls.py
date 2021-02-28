from django.urls import path

from . import views

urlpatterns = [
    path('selectCliente/', views.selectCliente, name='seleccion_Cliente'),
    path('selectProducto/<int:cedula>/<str:total>', views.selectProducto, name='seleccion_Producto'),
    path('comprar/<int:cedula>/<int:codigo>/<str:total>/', views.comprar, name='comprar'),
    path('terminarCompra/<int:cedula>/<str:total>', views.terminarCompra, name='terminar_Compra'),
]