from django.contrib import admin
from django.urls import path, include
from portal import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.lista_mascotas, name='home'),
    path('mascotas/', views.lista_mascotas, name='lista_mascotas'),
    path('adopcion/', views.solicitar_adopcion, name='solicitar_adopcion'),
    path('adopcion/<int:mascota_id>/', views.solicitar_adopcion, name='solicitar_adopcion_mascota'),
     path('', include("portal.urls")),
]
