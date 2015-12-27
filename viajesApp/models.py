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
