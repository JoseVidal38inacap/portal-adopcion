from django.contrib import admin
from .models import Mascota, Solicitante, SolicitudAdopcion

admin.site.register(Mascota)
admin.site.register(Solicitante)
admin.site.register(SolicitudAdopcion)
