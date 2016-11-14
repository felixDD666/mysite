from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


class Cliente(models.Model):
    Nombre = models.CharField(max_length=200)
    Apellido1 = models.CharField(max_length=200)
    Apellido2 = models.CharField(max_length=200)
    Telefono = models.CharField(max_length=200)
    Email = models.EmailField(max_length=200)
    Domicilio = models.CharField(max_length=200)
    Fecha_Nacimiento = models.CharField(max_length=200)
    Antecedentes_Personales = models.TextField()
    Antecedentes_Familiares = models.TextField()
    Historia_Clinica = models.TextField()
    Dia_registro = models.DateTimeField('date published')
    def __str__(self):
        return self.Nombre
        
    def was_published_recently(self):
        return self.Dia_registro >= timezone.now() - datetime.timedelta(days=1)

class Visita(models.Model):
    Cliente = models.CharField(max_length=200)
    Apellido1 = models.CharField(max_length=200)
    Apellido2 = models.CharField(max_length=200)
    Diagnostico = models.TextField()
    Tratamiento = models.TextField()
    Observaciones = models.TextField()
    Dia = models.DateTimeField('date') 
    def __str__(self):
        return self.Cliente

    def was_published_recently(self):
        return self.Dia_registro >= timezone.now() - datetime.timedelta(days=1)


class Categoria(models.Model):
    name = models.CharField(max_length=200)
    dateOfCreation = models.DateTimeField('date')

    def __str__(self):
        return self.name

class Post(models.Model):
    Titulo = models.CharField(max_length=200)
    Contenido = models.TextField()
    Categoria = models.ForeignKey(Categoria)
    Fecha_Creacion = models.DateTimeField('date')
    PUBLICO = 'pub'
    PRIVADO = 'pri'
    pORp_choices = (
        (PUBLICO, 'publico'),
        (PRIVADO, 'privado'),
    )
    Publico_Privado = models.CharField(
        max_length=3,
        choices=pORp_choices,
        default=PUBLICO,
    )
    Foto = models.ImageField(upload_to='postPhotos', default = 'SOMETHING')
    def __str__(self):
        return self.Titulo

        
class Mensaje(models.Model):
    nombre = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    telefono = models.CharField(max_length=200)
    mensaje = models.TextField();

    def __str__(self):
        return self.nombre