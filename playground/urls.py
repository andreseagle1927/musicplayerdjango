from django.urls import path
from . import views

#URL CONFIGURATION  

urlpatterns = [
   
    path("paginaFriend/", views.friend),
    path("sumar/id=1/", views.sumar1),
    path("sumar/id=2/", views.sumar2),
    path("sumar/id=3/", views.sumar3),
    path("sumar/id=4/", views.sumar4),
    path("sumar/id=5/", views.sumar5),
    path("sumar/id=6/", views.sumar6),


]