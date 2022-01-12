from django.db.models import fields
from django.urls import reverse_lazy
from django.db import models
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from applications.departamento.models import departamento
from.models import empleado
from.forms import empleadoForm
# Create your views here.


class InicioView(TemplateView):
    template_name = 'inicio.html'


class ListAllEmpleados(ListView):
    template_name = 'persona/lista-all.html'
    #model = empleado
    paginate_by = 4
    ordering = 'firstname'

    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword', '')
        lista = empleado.objects.filter(fullname__icontains=palabra_clave)
        return lista


class ListaEmpleadosAdmin(ListView):
    template_name = 'persona/lista-empleados.html'
    model = empleado
    paginate_by = 4
    ordering = 'firstname'


class ListabyArea(ListView):
    template_name = 'persona/ListabyArea.html'

    def get_queryset(self):
        area = self.kwargs['shortname']
        lista = empleado.objects.filter(departamento__shortname=area)
        return lista


class ListaempleadosbyKwargs(ListView):
    template_name = 'persona/byKwargs.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        print('*****************')
        palabra_clave = self.request.GET.get('kword', '')
        lista = empleado.objects.filter(firstname=palabra_clave)
        print('==================', palabra_clave)
        return lista


class habilidadesEmpleado(ListView):
    template_name = 'persona/habilidades.html'
    context_object_name = 'habilidades'

    def get_queryset(self):
        Empleado = empleado.objects.get(id=2)
        return Empleado.habilidades.all()


class empladoDetailView(DetailView):
    model = empleado
    template_name = "persona/detailEmpleado.html"


class empleadoCreateView(CreateView):
    model = empleado
    template_name = "persona/add.html"
    form_class = empleadoForm
    success_url = reverse_lazy('persona_app:empleados-admin')

    def form_valid(self, form):
        empleado = form.save()
        empleado.fullname = empleado.firstname + ' ' + empleado.lastname
        empleado.save()
        return super(empleadoCreateView, self).form_valid(form)


class successView(TemplateView):
    template_name = "persona/success.html"


class empleadoUpdateView(UpdateView):
    model = empleado
    template_name = 'persona/update.html'
    fields = ('__all__')
    success_url = reverse_lazy('persona_app:empleados-admin')

    def post(self, request, *args, **kwargs):
        self.objects = self.get_object()
        print('METODO POST')
        print(request.POST)
        print(request.POST['lastname'])
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        print('METODO FORM')
        return super(empleadoUpdateView, self).form_valid(form)


class empleadoDeleteView(DeleteView):
    model = empleado
    template_name = "persona/delete.html"
    success_url = reverse_lazy('persona_app:empleados-admin')
