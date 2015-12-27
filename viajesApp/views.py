from django.shortcuts import render
from django.template import RequestContext, loader
# Create your views here.
from django.http import HttpResponse

def index(request):
    contenido = {'nombre_sitio': 'Organizando Viajes com'}

    return render(request, 'viajesApp/index.html', contenido)