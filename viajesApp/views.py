from django.shortcuts import render, get_object_or_404
from django.template import RequestContext, loader
from .forms import ViajeForm, DestinoForm
# Create your views here.
from django.http import HttpResponse
from .models import Viaje, Destino
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
@login_required
def viaje_list(request):

    viajes = Viaje.objects.all()
    return render(request, 'viajesApp/viaje_list.html', {'viajes': viajes})
@login_required
def viaje_detail(request,pk):
    viaje = get_object_or_404(Viaje,pk=pk)

    return render(request,'viajesApp/viaje_detail.html', {'viaje': viaje})

@login_required
def viaje_new(request):

    if request.method == "POST":
        form = ViajeForm(request.POST)
        if form.is_valid():
            viaje = form.save(commit=False)
            viaje.author = request.user
            viaje.save()
            return redirect('viajesApp.views.viaje_detail', pk=viaje.pk)
    else:
        form = ViajeForm()
    return render(request, 'viajesApp/viaje_edit.html', {'form': form,'bootstrap':3})

@login_required
def viaje_edit(request, pk):
    viaje = get_object_or_404(Viaje, pk= pk)
    if request.method == "POST":
        form = ViajeForm(request.POST, instance=viaje)
        if form.is_valid():
            viaje = form.save(commit=False)
            viaje.author = request.user
            viaje.save()
            return redirect('viajesApp.views.viaje_detail', pk=viaje.pk)
    else:
        form = ViajeForm(instance=viaje)
    return render(request, 'viajesApp/viaje_edit.html', {'form': form, 'bootstrap':3})

@login_required
def viaje_remove(request, pk):
    viaje = get_object_or_404(Viaje, pk=pk)
    viaje.delete()
    return redirect('viajesApp.views.viaje_list')


def add_destino_to_viaje(request,pk):
    viaje = get_object_or_404(Viaje, pk=pk)
    if request.method == "POST":
        form = DestinoForm(request.POST)
        if form.is_valid():
            destino = form.save(commit=False)
            destino.viaje = viaje
            destino.save()
            return redirect('viajesApp.views.viaje_detail', pk=viaje.pk)
    else:
        form = DestinoForm()
    return render(request, 'viajesApp/add_destino_to_viaje.html',{'form': form})

def destino_remove(request, pk):
    destino = get_object_or_404(Destino, pk=pk)
    viaje = get_object_or_404(Viaje,pk=destino.viaje_id)
    destino.delete()
    return render(request,'viajesApp/viaje_detail.html', {'viaje': viaje})

def destino_edit(request, pk):
    destino = get_object_or_404(Destino, pk= pk)
    viaje = get_object_or_404(Viaje,pk=destino.viaje_id)
    if request.method == "POST":
        form = DestinoForm(request.POST, instance=destino)
        if form.is_valid():
            destino = form.save(commit=False)
            destino.save()
            return render(request,'viajesApp/viaje_detail.html', {'viaje': viaje})
    else:
        form = DestinoForm(instance=destino)
    return render(request, 'viajesApp/destino_edit.html', {'form': form, 'bootstrap':3})

