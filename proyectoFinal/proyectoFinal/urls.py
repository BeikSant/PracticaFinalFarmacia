from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clientes/', include('apps.gestion_clientes.urls')),
    path('productos/', include('apps.gestion_productos.urls')),
    path('comprarProducto/', include('apps.compra_farmacia.urls')),
    path('login/', include('apps.login.urls')),
    path('', views.index, name='homepage'),
]
