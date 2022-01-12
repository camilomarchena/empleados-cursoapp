from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from.models import prueba
from.forms import pruebaForm

# Create your views here.


class pruebaCreateView(CreateView):
    model = prueba
    template_name = 'home/Prueba.html'
    form_class = pruebaForm
    success_url = '.'


class ResumeFoundationView(TemplateView):
    template_name = 'home/resume_foundation.html'
