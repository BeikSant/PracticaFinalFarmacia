from django import forms
from apps.modelo.models import Cliente

class FormularioCliente(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ["cedula","apellidos","nombres","genero","correo","telefono","direccion"]
