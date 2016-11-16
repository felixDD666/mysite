from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


class Cliente(models.Model):
    Nombre = models.CharField(max_length=200)
    Primer_Apellido = models.CharField(max_length=200)
    Segundo_Apellido = models.CharField(max_length=200)
    Telefono = models.CharField(max_length=200)
    Email = models.EmailField(max_length=200)
    Domicilio = models.CharField(max_length=200)
    Fecha_Nacimiento = models.DateField()
    Antecedentes_Personales = models.TextField()
    Antecedentes_Familiares = models.TextField()
    Historia_Clinica = models.TextField('Historia Clinica')
    Dia_registro = models.DateTimeField('Fecha')
    def __str__(self):
        return self.Nombre + " " + self.Primer_Apellido + " " + self.Segundo_Apellido
        
    def was_published_recently(self):
        return self.Dia_registro >= timezone.now() - datetime.timedelta(days=1)

class Visita(models.Model):
    Cliente = models.ForeignKey(Cliente)
    Diagnostico = models.TextField()
    Tratamiento = models.TextField()
    Observaciones = models.TextField()
    Dia = models.DateField("Dia de la visita") 

    def was_published_recently(self):
        return self.Dia_registro >= timezone.now() - datetime.timedelta(days=1)


class Categoria(models.Model):
    Nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.Nombre



        
class Mensaje(models.Model):
    Nombre = models.CharField(max_length=200)
    Email = models.CharField(max_length=200)
    Telefono = models.CharField(max_length=200)
    Mensaje = models.TextField();

