from django.contrib import admin

from .models import *
from django.utils import timezone



class ClientesAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['Nombre','Primer_Apellido','Segundo_Apellido','Telefono','Email','Domicilio','Fecha_Nacimiento','Antecedentes_Personales','Antecedentes_Familiares','Historia_Clinica']}),
        ('Fecha de Creacion', {'fields': ['Dia_registro']}),
    ]
    list_display = ('Nombre','Primer_Apellido','Segundo_Apellido','Telefono','Email','Domicilio','Fecha_Nacimiento','Antecedentes_Personales','Antecedentes_Familiares','Historia_Clinica', 'Dia_registro')
    list_filter = ['Dia_registro']
    search_fields = ['Nombre']


admin.site.register(Cliente, ClientesAdmin)


class VisitasAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,               {'fields': ['Cliente','Diagnostico','Tratamiento','Observaciones']}),
		('Fecha', {'fields': ['Dia']}),
	]
	list_display = ('Cliente','Diagnostico','Tratamiento', 'Observaciones', 'Dia')
	list_filter = ['Dia']
	search_fields = ['Cliente']


admin.site.register(Visita, VisitasAdmin)  



class MensajesAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,{'fields': ['Nombre','Email','Telefono','Mensaje']}),
		
	]
	list_display = ('Nombre', 'Email', 'Telefono' , 'Mensaje')
	
	search_fields = ['Nombre']


admin.site.register(Mensaje, MensajesAdmin)