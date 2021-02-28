from django.shortcuts import render, redirect
from .forms import FormularioLogin
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect

def autenticar(request):
    if request.method == 'POST':
        formulario = FormularioLogin(request.POST)
        if formulario.is_valid():
            usuario = request.POST['username']
            clave = request.POST['password']
            user = authenticate(username=usuario, password=clave)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect(welcome)
                else:
                    return HttpResponseRedirect(redirect('no_activo'))
            else:
                return redirect(desactivado)
    else:
        formulario = FormularioLogin()
    context = {
        'formulario': formulario
    }
    return render(request, 'login/login.html', context)


def desautenticar(request):
    usuario = request.user
    logout(request)
    return redirect('homepage')


def welcome(request):
    return render(request, 'login/welcome.html')


def forbidden(request):
    return render(request, 'login/forbidden.html')


def desactivado(request):
    return render(request, 'login/desactive.html')
