from django import forms
from apps.modelo.models import Compra

class FormularioCompra(forms.ModelForm):
    class Meta:
        model = Compra
        fields = ["numero_Productos","descripcion"]
