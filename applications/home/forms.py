from django import forms
from django.forms import widgets
from.models import prueba


class pruebaForm(forms.ModelForm):
    """Form definition for prueba."""

    class Meta:
        """Meta definition for pruebaform."""

        model = prueba
        fields = ('__all__')
        widgets = {'titulo': forms.TextInput(
            attrs={'placeholder': 'Ingrese texto aquí'})}

    def clean_cantidad(self):
        cantidad = self.cleaned_data['cantidad']
        if cantidad < 10:
            raise forms.ValidationError('Ingrese un número mayor a 10 ')
        return cantidad
