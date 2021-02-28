from apps.modelo.models import Producto
from .forms import FormularioProducto
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, User


@login_required
def index(request):
    usuario = request.user
    if usuario.groups.filter(name='gestion_farmacia').exists():
        # manejo del ORM
        listaProductos = Producto.objects.all()
        return render(request, 'productos/index.html', locals())
    else:
        return render(request, 'login/forbidden.html', locals())


@login_required
def crearProducto(request):
    usuario = request.user
    if usuario.groups.filter(name='gestion_farmacia').exists():
        formulario_producto = FormularioProducto(request.POST)
        if request.method == 'POST':
            if formulario_producto.is_valid():
                producto = Producto()
                datos_producto = formulario_producto.cleaned_data
                producto.codigo = datos_producto.get('codigo')
                producto.nombre = datos_producto.get('nombre')
                producto.stock = datos_producto.get('stock')
                producto.precio_Unitario = datos_producto.get('precio_Unitario')
                # ORM
                producto.save()
            return redirect(index)
        return render(request, 'productos/crear.html', locals())
    else:
        return render(request, 'login/forbidden.html', locals())


@login_required
def modificarProducto(request, codigo):
    usuario = request.user
    if usuario.groups.filter(name='gestion_farmacia').exists():
        producto = Producto.objects.get(codigo=codigo)
        if request.method == 'GET':
            formulario_producto = FormularioProducto(instance=producto)
        else:
            formulario_producto = FormularioProducto(
                request.POST, instance=producto)
            if formulario_producto.is_valid():
                # ORM
                formulario_producto.save()
            return redirect(index)
        return render(request, 'productos/modificar.html', locals())
    else:
        return render(request, 'login/forbidden.html', locals())


@login_required
def eliminarProducto(request, codigo):
    usuario = request.user
    if usuario.groups.filter(name='gestion_farmacia').exists():
        producto = Producto.objects.get(codigo=codigo)
        producto.delete()
        return redirect(index)
    else:
        return render(request, 'login/forbidden.html', locals())