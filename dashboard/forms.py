from django import forms
from .models import Reporte

class ReporteForm(forms.ModelForm):
    class Meta:
        model = Reporte
        fields = ['titulo', 'descripcion']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }