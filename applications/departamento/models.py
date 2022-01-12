from django.db import models

# Create your models here.


class departamento(models.Model):
    name = models.CharField('Nombre', max_length=50, unique=True)
    shortname = models.CharField(
        'Nombre corto', max_length=20, blank=True, unique=True)
    anulate = models.BooleanField('anulado', default=False)

    class Meta:
        verbose_name = 'Mis departamentos'
        verbose_name_plural = 'Áreas de la empresa'
        ordering = ['name']
        unique_together = ('name', 'shortname')

    def __str__(self):
        return self.name + ' - ' + self.shortname
