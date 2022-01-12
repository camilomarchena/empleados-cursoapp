from applications.persona.models import empleado
from django.forms import forms
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import FormView
from.forms import newdepartamentoforms
from.models import departamento

# Create your views here.


class DepartamentoListView(ListView):
    model = departamento
    template_name = "departamento/lista.html"


class pruebaListView(ListView):
    context_object_name = "Lista_numeros"
    queryset = ['1', '2', '3', '4', '5']
    template_name = "departamento/prueba.html"


class newdepartamento(FormView):
    template_name = 'departamento/new-departamento.html'
    form_class = newdepartamentoforms
    success_url = '.'

    def form_valid(self, form):
        depa = departamento(
            name=form.cleaned_data['departamento'], shortname=form.cleaned_data['shortname'])
        depa.save()
        nombre = form.cleaned_data['nombre']
        apellido = form.cleaned_data['apellidos']
        empleado.objects.create(
            firstname=nombre, lastname=apellido, job='1', departamento=depa)
        return super(newdepartamento, self).form_valid(form)
