from django.conf.urls import url

from . import views

app_name = 'polls'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^principal/$', views.principal, name='principal'),
    url(r'^principal/formacionC/$', views.formacionC, name='formacionC'),
    url(r'^principal/servicio1/$', views.servicio1, name='servicio1'),
    url(r'^principal/servicio2/$', views.servicio2, name='servicio2'),
    url(r'^principal/servicio3/$', views.servicio3, name='servicio3'),
    url(r'^principal/servicio4/$', views.servicio4, name='servicio4'),
    url(r'^principal/servicio5/$', views.servicio5, name='servicio5'),
    url(r'^principal/servicio6/$', views.servicio6, name='servicio6'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]

#hola que tal 