from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
#EMAILS
from django.core.mail import send_mail
from .forms import ContactForm
from .models import *
from django.views.decorators.clickjacking import xframe_options_exempt


from django.utils import timezone


def principal(request):
    posts = Post.objects.order_by("-Fecha_Creacion")
    numPost = Post.objects.count()-3;
    return render(request,'polls/principal.html',{
        "posts":posts,
        "numPost": numPost
        })

def formacionC(request):
    return render(request,'polls/formacionC.html',{})

def servicio1(request):
    return render(request,'polls/servicio1.html',{})

def servicio2(request):
    return render(request,'polls/servicio2.html',{})

def servicio3(request):
    return render(request,'polls/servicio3.html',{})

def servicio4(request):
    return render(request,'polls/servicio4.html',{})
 
def servicio5(request):
    return render(request,'polls/servicio5.html',{})
    
def servicio6(request):
    return render(request,'polls/servicio6.html',{})

def EventosCalendar(request):
    return render(request,'polls/EventosCalendar.html',{})

def homePosts(request):
    posts = Post.objects.order_by("-Fecha_Creacion")
    categories = Categoria.objects.order_by("Nombre")
    return render(request,'polls/homePosts.html',{
            "posts":posts,
            "categories":categories,
        },
    )

def one_post(request, idpost):
    posts = Post.objects.get(id=idpost)

    return render(request,'polls/post.html',{
            "post":posts,
        },
    )

"""
def posts_by_category(request, idcategory):
    category = Category.objects.get(id=idcategory)
    posts = category.post_set.order_by("-Fecha_Creacion")

    return render_to_response(
        "home.html",
        {
            "posts":posts,
        },
    )
"""
def contacta(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():

            nombre = form.cleaned_data['nombre']
            email = form.cleaned_data['email']
            telefono = form.cleaned_data['telefono']
            mensaje = form.cleaned_data['mensaje']
            newMensaje = Mensaje(Nombre = nombre, Email = email, Telefono = telefono, Mensaje = mensaje)
            try:
                send_mail("Nuevo mensaje de " + nombre, "Email: " + email + "\n\nTelefono: " + telefono + "\n\nContenido: " + mensaje , 'podoAlvaro@gmail.com', ['agpodologia@gmail.com'])
                newMensaje.save()
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return HttpResponseRedirect("thanks")
    return render(request, "polls/contacta.html", {'form': form})

def thanks(request):
    return render(request,'polls/thanks.html',{})

