from django import forms
from .models import Productos

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = ['nombre', 'price', 'disponible']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'disponible': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }