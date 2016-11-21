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
        
    

class Visita(models.Model):
    Cliente = models.ForeignKey(Cliente)
    Diagnostico = models.TextField()
    Tratamiento = models.TextField()
    Observaciones = models.TextField()
    Dia = models.DateField("Dia de la visita") 



class Categoria(models.Model):
    Nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.Nombre

class Post(models.Model):
    Titulo = models.CharField(max_length=200)
    Contenido = models.TextField()
    Categoria = models.ForeignKey(Categoria)
    Fecha_Creacion = models.DateTimeField('Fecha de creacion')
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
    Nombre = models.CharField(max_length=200)
    Email = models.CharField(max_length=200)
    Telefono = models.CharField(max_length=200)
    Mensaje = models.TextField();

