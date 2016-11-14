from django.contrib import admin

from .models import *
from django.utils import timezone


class ClientesAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['Nombre','Apellido1','Apellido2','Telefono','Email','Domicilio','Fecha_Nacimiento','Antecedentes_Personales','Antecedentes_Familiares','Historia_Clinica']}),
        ('Fecha de Creacion', {'fields': ['Dia_registro']}),
    ]
    list_display = ('Nombre','Apellido1','Apellido2','Telefono','Email','Domicilio','Fecha_Nacimiento','Antecedentes_Personales','Antecedentes_Familiares','Historia_Clinica', 'Dia_registro')
    list_filter = ['Dia_registro']
    search_fields = ['Nombre']


admin.site.register(Cliente, ClientesAdmin)


class VisitasAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,               {'fields': ['Cliente','Apellido1','Apellido2','Diagnostico','Tratamiento','Observaciones']}),
		('Date information', {'fields': ['Dia']}),
	]
	list_display = ('Cliente','Apellido1','Apellido2','Diagnostico','Tratamiento', 'Observaciones', 'Dia')
	list_filter = ['Dia']
	search_fields = ['Cliente','Apellido1','Apellido2']


admin.site.register(Visita, VisitasAdmin)  

class CategoryAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,               {'fields': ['name']}),
		('Date information', {'fields': ['dateOfCreation']}),
	]
	list_display = ('name', 'dateOfCreation')
	list_filter = ['dateOfCreation']
	search_fields = ['name']

admin.site.register(Categoria, CategoryAdmin)


class PostsAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,               {'fields': ['Titulo','Contenido','Categoria','Publico_Privado','Foto']}),
		('Date information', {'fields': ['Fecha_Creacion']}),
	]
	list_display = ('Titulo', 'Contenido', 'Fecha_Creacion' , 'Categoria','Foto')
	list_filter = ['Fecha_Creacion']
	search_fields = ['Titulo']


admin.site.register(Post, PostsAdmin)

class MensajesAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,{'fields': ['nombre','email','telefono','mensaje']}),
		
	]
	list_display = ('nombre', 'email', 'telefono' , 'mensaje')
	
	search_fields = ['nombre']


admin.site.register(Mensaje, MensajesAdmin)
