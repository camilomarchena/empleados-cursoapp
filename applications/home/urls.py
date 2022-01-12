from django.conf import settings
from django.urls import path
from django.contrib import admin
from. import views

urlpatterns = [
    path('Prueba/', views.pruebaCreateView.as_view()),
    path('resume/', views.ResumeFoundationView.as_view(), name='resume_foundation'),
]
