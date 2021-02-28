from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='productos'),
    path('crearProducto', views.crearProducto, name='crear_producto'),
    path('modificarProducto/<int:codigo>/', views.modificarProducto, name='modificar_producto'),
    path('eliminarProducto/<int:codigo>/', views.eliminarProducto, name='eliminar_producto'),
]

