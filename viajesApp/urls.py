from django.conf.urls import patterns, url
from viajesApp import views


urlpatterns = patterns('',
url(r'^$', views.viaje_list, name='viaje_list'),
url (r'^viaje/(?P<pk>[0-9]+)/$', views.viaje_detail),
url(r'^viaje/new/$', views.viaje_new, name='viaje_new'),
url(r'^viaje/(?P<pk>[0-9]+)/edit/$', views.viaje_edit, name='viaje_edit'),
url(r'^viaje/(?P<pk>[0-9]+)/remove/$', views.viaje_remove, name='viaje_remove'),
url(r'^viaje/(?P<pk>[0-9]+)/destino/$', views.add_destino_to_viaje, name='add_destino_to_viaje'),
url(r'^viaje/(?P<pk>[0-9]+)/destino/remove/$', views.destino_remove, name='destino_remove'),
url(r'^viaje/(?P<pk>[0-9]+)/destino/edit/$', views.destino_edit, name='destino_edit'),
)