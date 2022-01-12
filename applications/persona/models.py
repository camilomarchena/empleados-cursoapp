from django.db import models
from django.db.models.base import Model
from applications.departamento.models import departamento


# Create your models here.


class Habilidades(models.Model):
    habilidad = models.CharField('Habilidades', max_length=20)

    class Meta:
        verbose_name = 'Habilidades'
        verbose_name_plural = 'Habilidades empleados'

    def __str__(self):
        return self.habilidad


class empleado(models.Model):
    JOB_CHOICES = (('0', 'Contador'), ('1', 'Administrador'),
                   ('2', 'Economista'), ('3', 'Otro'))
    firstname = models.CharField('Primer nombre', max_length=50)
    lastname = models.CharField('Apellido', max_length=50)
    job = models.CharField('Trabajo', max_length=1, choices=JOB_CHOICES)
    departamento = models.ForeignKey(departamento, on_delete=models.CASCADE)
    habilidades = models.ManyToManyField(Habilidades)
    fullname = models.CharField('Nombre Completo', max_length=50, blank=True)
    avatar = models.ImageField(
        'Foto', upload_to='empleado', blank=True, null=True)

    class Meta:
        verbose_name = 'Personas'
        verbose_name_plural = 'Mis empleados'
        ordering = ['firstname']
        unique_together = ('firstname', 'lastname')

    def __str__(self):
        return self.firstname + ' ' + self.lastname
