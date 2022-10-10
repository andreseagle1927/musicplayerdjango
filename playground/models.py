from xml.dom.minidom import Entity
from django.db import models

# Create your models here.

class Cantante(models.Model):
    nombre = models.CharField(max_length = 100)
    img_cantante = models.CharField(max_length = 100)
    genero = models.CharField(max_length = 100)

    def __str__(self):
        return self.nombre
    
    
    


class Canciones(models.Model):
    nombreCancion= models.CharField(max_length = 100)
    genero = models.CharField(max_length = 100)

    #DECLARACION LLAVE FORANEA
    #Damos un modelo TIPO "Cantante"
    cantante = models.ForeignKey(Cantante, on_delete=models.CASCADE)

    link = models.CharField(max_length = 100)

    duracion = models.CharField(max_length = 100)

    imgCancion = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.nombreCancion
    
    
