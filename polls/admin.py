from django.contrib import admin

from .models import *
from django.utils import timezone


class ClientesAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['Nombre','DNI','Hist']}),
        ('Date information', {'fields': ['Dia_registro'], 'classes': ['collapse']}),
    ]
    list_display = ('Nombre', 'DNI', 'Hist', 'Dia_registro')
    list_filter = ['Dia_registro']
    search_fields = ['Nombre']


admin.site.register(Cliente, ClientesAdmin)


class CitasAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,               {'fields': ['Nombre','Cliente','Observaciones']}),
		('Date information', {'fields': ['Dia'], 'classes': ['collapse']}),
	]
	list_display = ('Nombre', 'Cliente', 'Observaciones', 'Dia')
	list_filter = ['Dia']
	search_fields = ['Nombre']


admin.site.register(Cita, CitasAdmin)  

class CategoryAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,               {'fields': ['name']}),
		('Date information', {'fields': ['dateOfCreation'], 'classes': ['collapse']}),
	]
	list_display = ('name', 'dateOfCreation')
	list_filter = ['dateOfCreation']
	search_fields = ['name']

admin.site.register(Categoria, CategoryAdmin)


class PostsAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,               {'fields': ['title','content','category']}),
		('Date information', {'fields': ['creation_date'], 'classes': ['collapse']}),
	]
	list_display = ('title', 'content', 'creation_date' , 'category')
	list_filter = ['creation_date']
	search_fields = ['title']


admin.site.register(Post, PostsAdmin)

class MensajesAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,               {'fields': ['nombre','email','telefono','mensaje']}),
		
	]
	list_display = ('nombre', 'email', 'telefono' , 'mensaje')
	
	search_fields = ['nombre']


admin.site.register(Mensaje, MensajesAdmin)
