from django.conf.urls import patterns, url
from viajesApp import views
urlpatterns = patterns('',
url(r'^$', views.index, name='index'),
)