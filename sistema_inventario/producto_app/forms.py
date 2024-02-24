# forms.py
from django import forms
from .models import *

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'fk_categoria', 'fk_estado', 'fk_marca', 'fk_proveedor', 'descripcion', 'stock']

        labels = {
            'nombre': 'Nombre',
            'precio': 'Precio',
            'fk_categoria': 'Categoria',
            'fk_estado': 'Estado',
            'fk_marca': 'Marca',
            'fk_proveedor': 'Proveedor',
            'descripcion': 'Descripcion'

        }





class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'descripcion', 'fk_estado']
        labels = {
            'fk_esatdo': 'Estado',
        }






class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['nombre', 'descripcion', 'fk_estado']
        labels = {
            'fk_esatdo': 'Estado',
        }

class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = ['nombre', 'descripcion', 'fk_estado']
        labels = {
            'fk_esatdo': 'Estado',
        }