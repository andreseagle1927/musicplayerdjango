from django.urls import path
from . import views

#URL CONFIGURATION  

urlpatterns = [
   
    path("paginaFriend/", views.friend),
    path("spotify/", views.spo)
]