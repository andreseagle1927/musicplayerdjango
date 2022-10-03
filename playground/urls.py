from django.urls import path
from . import views

#URL CONFIGURATION  

urlpatterns = [
    path("hello/", views.say_hello),
    path("home/", views.home),
    path("main/", views.main),
    path("paginaFriend/", views.friend),
    path("spotify/", views.spo)
]