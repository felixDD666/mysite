from django.conf.urls import url

from . import views

app_name = 'polls'
urlpatterns = [
    url(r'^$', views.principal, name='principal'),
    url(r'^formacionC/$', views.formacionC, name='formacionC'),
    url(r'^servicio1/$', views.servicio1, name='servicio1'),
    url(r'^servicio2/$', views.servicio2, name='servicio2'),
    url(r'^servicio3/$', views.servicio3, name='servicio3'),
    url(r'^servicio4/$', views.servicio4, name='servicio4'),
    url(r'^servicio5/$', views.servicio5, name='servicio5'),
    url(r'^servicio6/$', views.servicio6, name='servicio6'),
    url(r'^allPosts/$', views.homePosts, name='one_post'),
    url(r'^(?P<idpost>[0-9]+)/$', views.one_post, name='one_post'),
    url(r'^allPosts/(?P<idpost>[0-9]+)/$', views.one_post, name='one_post'),
    url(r'^contacta/$',views.contacta,name='contacta'),
    url(r'^thanks/$',views.thanks,name='thanks'),
]

    #url(r'^$', views.IndexView.as_view(), name='index'),
    #url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    #url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    #url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
