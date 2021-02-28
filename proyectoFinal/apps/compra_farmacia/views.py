from apps.modelo.models import Compra, Producto, Cliente
from .forms import FormularioCompra
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


@login_required
def selectCliente(request):
    usuario = request.user
    if usuario.groups.filter(name='gestion_farmacia').exists():
        # manejo del ORM
        listaClientes = Cliente.objects.all()
        return render(request, 'compra/selectCliente.html', locals())
    else:
        return render(request, 'login/forbidden.html', locals())


@login_required
def selectProducto(request, cedula, total):
    cliente = Cliente.objects.get(cedula=cedula)
    usuario = request.user
    if usuario.groups.filter(name='gestion_farmacia').exists():
        listaProductos = Producto.objects.all()
        return render(request, 'compra/selectProducto.html', locals())
    else:
        return render(request, 'login/forbidden.html', locals())

@login_required
def comprar(request, cedula, codigo, total):
    usuario = request.user
    if usuario.groups.filter(name='gestion_farmacia').exists():
        formulario_compra = FormularioCompra(request.POST)
        cliente = Cliente.objects.get(cedula=cedula)
        producto = Producto.objects.get(codigo=codigo)
        if request.method == 'POST':
            print(formulario_compra.is_valid())
            if formulario_compra.is_valid():
                compra = Compra()
                datos_compra = formulario_compra.cleaned_data
                compra.numero_Productos = datos_compra.get('numero_Productos')
                compra.descripcion = datos_compra.get('descripcion')
                compra.cliente = cliente
                compra.product = producto
                compra.valor_Total = compra.numero_Productos * producto.precio_Unitario
                if compra.numero_Productos <= producto.stock:
                    producto.stock = producto.stock-compra.numero_Productos
                    pt = float(total) + float(compra.valor_Total)
                    total = str(pt)
                    compra.save()
                    producto.save()
                    return redirect(selectProducto, cedula, total)
                else:
                    mensaje = "No existen productos suficientes"
        return render(request, 'compra/comprarProducto.html', locals())
    else:
        return render(request, 'login/forbidden.html', locals())

@login_required
def terminarCompra(request,cedula,total):
    usuario = request.user
    if usuario.groups.filter(name='gestion_farmacia').exists():
        cliente = Cliente.objects.get(cedula=cedula)
        return render(request, 'compra/totalCompra.html', locals())
    else:
        return render(request, 'login/forbidden.html', locals())

