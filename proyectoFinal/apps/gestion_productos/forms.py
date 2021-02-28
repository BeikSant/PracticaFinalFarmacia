from django import forms
from apps.modelo.models import Producto

class FormularioProducto(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ["codigo","nombre","stock","precio_Unitario"]