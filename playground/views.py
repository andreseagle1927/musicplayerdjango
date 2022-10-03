import django
from django.shortcuts import render
from django.http import HttpResponse

def say_hello(request):
    return render(request, "hello.html", {"name": "german", "sport" : "Homew"})

def home(request):
    return render(request, "home.html")

def room(request):
    return render(request, "room.html")

def main(request):
    return render(request, "main.html")

def friend(request):
    return render(request, "hello.html", {"name": "PAGINA", "sport" : "FRIEND"})

def spo(request):
    return render(request, "index.html")





