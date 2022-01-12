from django import forms
from.models import empleado


class empleadoForm(forms.ModelForm):
    """Form definition for empleado."""

    class Meta:
        """Meta definition for empleadoform."""

        model = empleado
        fields = ('firstname', 'lastname', 'job',
                  'departamento', 'avatar', 'habilidades')
        widgets = {
            'habilidades': forms.CheckboxSelectMultiple()
        }
