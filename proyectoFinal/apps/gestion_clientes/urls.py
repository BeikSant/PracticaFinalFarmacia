from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='clientes'),
    path('crearClientes', views.crearCliente, name='crear_cliente'),
    path('modificarCliente/<int:cedula>/', views.modificarCliente, name='modificar_cliente'),
    path('eliminarCliente/<int:cedula>/', views.eliminarCliente, name='eliminar_cliente'),
]

