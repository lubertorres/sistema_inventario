# forms.py
from django import forms
from .models import *

class CLienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'cedula', 'correo', 'edad', 'celular', 'fk_estado']
        labels = {
            'fk_estado': 'Estado',
        }