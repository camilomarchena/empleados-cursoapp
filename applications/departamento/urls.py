from django.urls import path
from django.contrib import admin
from.import views

app_name = 'departamento_app'


urlpatterns = [
    path('list/', views.pruebaListView.as_view()),
    path('new-departamento/', views.newdepartamento.as_view(),
         name='nuevo_departamento'),
    path('departamento/', views.DepartamentoListView.as_view(),
         name='departamento-list'),
]
