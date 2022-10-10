import django
from django.shortcuts import render
from django.http import HttpResponse

from playground.models import Canciones, Cantante




def friend(request):
    return render(request, "hello.html", {"name": "PAGINA", "sport" : "FRIEND"})

def spo(request):
    cantantes = Cantante.objects.filter(nombre= "anuel")
    return render(request, "index.html", {"name": cantantes})







