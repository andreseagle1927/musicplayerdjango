import django
from django.shortcuts import render
from django.http import HttpResponse
from playground.models import Cantante, Canciones

#from playground.models import Canciones, Cantante




def friend(request):
    return render(request, "index.html")



def sumar1(request):
    cancionEditar = Canciones.objects.get(idcancion = 1)
    cancionEditar.plays = cancionEditar.plays + 1
    playsCancion = cancionEditar.plays
    nombreCancion = cancionEditar.nombrecancion
    linkCancion = cancionEditar.link
    cancionEditar.save()
    return render(request,"index.html", {"nombreCancion": nombreCancion, "playsCancion" : playsCancion, "id" : cancionEditar.idcancion, "link":linkCancion})

def sumar2(request):
    cancionEditar = Canciones.objects.get(idcancion = 2)
    cancionEditar.plays = cancionEditar.plays + 1
    playsCancion = cancionEditar.plays
    nombreCancion = cancionEditar.nombrecancion
    linkCancion = cancionEditar.link
    cancionEditar.save()
    return render(request,"index.html", {"nombreCancion": nombreCancion, "playsCancion" : playsCancion, "id" : cancionEditar.idcancion, "link":linkCancion})

def sumar3(request):
    cancionEditar = Canciones.objects.get(idcancion = 3 )
    cancionEditar.plays = cancionEditar.plays + 1
    playsCancion = cancionEditar.plays
    nombreCancion = cancionEditar.nombrecancion
    linkCancion = cancionEditar.link
    cancionEditar.save()
    return render(request,"index.html", {"nombreCancion": nombreCancion, "playsCancion" : playsCancion, "id" : cancionEditar.idcancion, "link":linkCancion})

def sumar4(request):
    cancionEditar = Canciones.objects.get(idcancion = 4)
    cancionEditar.plays = cancionEditar.plays + 1
    playsCancion = cancionEditar.plays
    nombreCancion = cancionEditar.nombrecancion
    linkCancion = cancionEditar.link
    cancionEditar.save()
    return render(request,"index.html", {"nombreCancion": nombreCancion, "playsCancion" : playsCancion, "id" : cancionEditar.idcancion, "link":linkCancion})


def sumar5(request):
    cancionEditar = Canciones.objects.get(idcancion = 5)
    cancionEditar.plays = cancionEditar.plays + 1
    playsCancion = cancionEditar.plays
    nombreCancion = cancionEditar.nombrecancion
    linkCancion = cancionEditar.link
    cancionEditar.save()
    return render(request,"index.html", {"nombreCancion": nombreCancion, "playsCancion" : playsCancion, "id" : cancionEditar.idcancion, "link":linkCancion})


def sumar6(request):
    cancionEditar = Canciones.objects.get(idcancion = 6)
    cancionEditar.plays = cancionEditar.plays + 1
    playsCancion = cancionEditar.plays
    nombreCancion = cancionEditar.nombrecancion
    linkCancion = cancionEditar.link
    cancionEditar.save()
    return render(request,"index.html", {"nombreCancion": nombreCancion, "playsCancion" : playsCancion, "id" : cancionEditar.idcancion, "link":linkCancion})





