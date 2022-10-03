from xml.dom.minidom import Entity
from django.db import models

# Create your models here.

class Cantante(models.Model):
    nombre = models.CharField(max_length = 100)
    genero = models.CharField(max_length = 100)
    img_cantante = models.CharField(max_length = 100)
    pais = models.CharField(max_length = 100)
    


class Canciones(models.Model):
    img_cancion = models.CharField(max_length = 100)
    nombreCancion= models.CharField(max_length = 100)
    duracion = models.CharField(max_length = 100)
    link = models.CharField(max_length = 100)
    genero = models.CharField(max_length = 100)
    cantante = models.CharField(max_length = 100)
