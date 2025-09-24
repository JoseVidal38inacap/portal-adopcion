from django.urls import path
from . import views

urlpatterns = [
    path("mascotas/", views.lista_mascotas, name="lista_mascotas"),
]
