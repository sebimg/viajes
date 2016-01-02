from django.db import models

# Create your models here.

class Viaje(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    hotel = models.CharField(max_length=50)
    destino = models.CharField(max_length=50)
    detalles = models.TextField()
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null= True)

    def publicar(self):
        self.save()

    def __str__(self):
        return self.title

class Destino(models.Model):
    nombre = models.CharField(max_length=50)
    comentario = models.TextField()
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null= True)
    hotel = models.CharField(max_length=50)
    viaje = models.ForeignKey('viajesApp.Viaje',related_name='destinos')

    def publicar(self):
        self.save()

    def __str__(self):
        return self.nombre

class Detalle(models.Model):
    nombre = models.CharField(max_length=50)
    detalle = models.TextField()
    destino = models.ForeignKey('viajesApp.Destino',related_name='detalles')

    def publicar(self):
        self.save()

    def __str__(self):
        return self.nombre