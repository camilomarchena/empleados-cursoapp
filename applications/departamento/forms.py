from django import forms


class newdepartamentoforms(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    apellidos = forms.CharField(max_length=50, required=True)
    departamento = forms.CharField(max_length=50, required=True)
    shortname = forms.CharField(max_length=20, required=True)
