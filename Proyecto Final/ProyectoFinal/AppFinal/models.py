from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Peliculas(models.Model):

    def __str__(self):

        return f"Nombre: {self.nombre} --- Duracion: {self.duracion}"

    nombre=models.CharField(max_length=40)
    duracion= models.IntegerField()

class Cines(models.Model):

    def __str__(self):

        return f"Nombre: {self.nombre} --- Ubicacion: {self.ubicacion}"

    nombre=models.CharField(max_length=40)
    ubicacion=models.CharField(max_length=40)


class Categoria(models.Model):

    category=models.CharField(max_length=40)

class Avatars(models.Model):

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)