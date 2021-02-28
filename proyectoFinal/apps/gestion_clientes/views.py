from apps.modelo.models import Cliente
from .forms import FormularioCliente
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, User


@login_required
def index(request):
    usuario = request.user
    if usuario.groups.filter(name='gestion_farmacia').exists():
        # manejo del ORM
        listaClientes = Cliente.objects.all()
        return render(request, 'clientes/index.html', locals())
    else:
        return render(request, 'login/forbidden.html', locals())


@login_required
def crearCliente(request):
    usuario = request.user
    if usuario.groups.filter(name='gestion_farmacia').exists():
        formulario_cliente = FormularioCliente(request.POST)
        if request.method == 'POST':
            if formulario_cliente.is_valid():
                cliente = Cliente()
                datos_cliente = formulario_cliente.cleaned_data
                cliente.cedula = datos_cliente.get('cedula')
                cliente.nombres = datos_cliente.get('nombres')
                cliente.apellidos = datos_cliente.get('apellidos')
                cliente.genero = datos_cliente.get('genero')
                cliente.correo = datos_cliente.get('correo')
                cliente.telefono = datos_cliente.get('telefono')
                cliente.direccion = datos_cliente.get('direccion')
                # ORM
                cliente.save()
                user = User.objects.create_user(
                    cliente.cedula, cliente.correo, cliente.cedula)
                user.first_name = cliente.nombres
                user.last_name = cliente.apellidos
                grupo = Group.objects.get(name='clientes')
                user.groups.add(grupo)
                user.save()

            return redirect(index)
        return render(request, 'clientes/crear.html', locals())
    else:
        return render(request, 'login/forbidden.html', locals())


@login_required
def modificarCliente(request, cedula):
    usuario = request.user
    if usuario.groups.filter(name='gestion_farmacia').exists():
        cliente = Cliente.objects.get(cedula=cedula)
        if request.method == 'GET':
            formulario_cliente = FormularioCliente(instance=cliente)
        else:
            formulario_cliente = FormularioCliente(
                request.POST, instance=cliente)
            if formulario_cliente.is_valid():
                # ORM
                formulario_cliente.save()
            return redirect(index)
        return render(request, 'clientes/modificar.html', locals())
    else:
        return render(request, 'login/forbidden.html', locals())


@login_required
def eliminarCliente(request, cedula):
    usuario = request.user
    if usuario.groups.filter(name='gestion_farmacia').exists():
        cliente = Cliente.objects.get(cedula=cedula)
        cliente.delete()
        return redirect(index)
    else:
        return render(request, 'login/forbidden.html', locals())
