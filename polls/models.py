from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


class Cliente(models.Model):
    Nombre = models.CharField(max_length=200)
    DNI = models.CharField(max_length=200)
    Hist = models.TextField()
    Dia_registro = models.DateTimeField('date published')
    def __str__(self):
        return self.Nombre
        
    def was_published_recently(self):
        return self.Dia_registro >= timezone.now() - datetime.timedelta(days=1)

class Cita(models.Model):
	Nombre = models.CharField(max_length=200)
	Cliente = models.CharField(max_length=200)
	Observaciones = models.TextField()
	Dia = models.DateTimeField('date')

	def __str__(self):
		return self.Nombre

	def was_published_recently(self):
		return self.Dia_registro >= timezone.now() - datetime.timedelta(days=1)


class Categoria(models.Model):
    name = models.CharField(max_length=200)
    dateOfCreation = models.DateTimeField('date')

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.ForeignKey(Categoria)
    creation_date = models.DateTimeField('date')

    def __str__(self):
        return self.title

        
class Mensaje(models.Model):
    nombre = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    telefono = models.CharField(max_length=200)
    mensaje = models.TextField();

    def __str__(self):
        return self.nombre