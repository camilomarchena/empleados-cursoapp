from django.urls import path
from django.contrib import admin
from. import views

app_name = 'persona_app'
urlpatterns = [
    path('', views.InicioView.as_view(), name='inicio'),
    path('lista-all/', views.ListAllEmpleados.as_view(), name='empleados_all'),
    path('listabyArea/<shortname>',
         views.ListabyArea.as_view(), name='empleados-area'),
    path('byKwargs/', views.ListaempleadosbyKwargs.as_view()),
    path('habilidadesEmpleado/', views.habilidadesEmpleado.as_view()),
    path('detailEmpleado/<pk>', views.empladoDetailView.as_view(),
         name='empleado-detail'),
    path('add/', views.empleadoCreateView.as_view(), name="empleado-add"),
    path('success/', views.successView.as_view(), name='success'),
    path('update/<pk>', views.empleadoUpdateView.as_view(), name='modificar'),
    path('delete/<pk>', views.empleadoDeleteView.as_view(), name='delete'),
    path('lista-empleados-admin/',
         views.ListaEmpleadosAdmin.as_view(), name='empleados-admin'),


]
