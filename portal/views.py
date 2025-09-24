from django.shortcuts import render, redirect, get_object_or_404
from .models import Mascota
from .forms import SolicitudAdopcionForm

def lista_mascotas(request):
    mascotas = Mascota.objects.all()
    return render(request, "portal/lista_mascotas.html", {"mascotas": mascotas})

def solicitar_adopcion(request, mascota_id=None):
    mascota = None
    if mascota_id:
        mascota = get_object_or_404(Mascota, id=mascota_id)

    if request.method == 'POST':
        form = SolicitudAdopcionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_mascotas')
    else:
        if mascota:
            # inicializa la mascota en el form
            form = SolicitudAdopcionForm(initial={'mascota': mascota})
        else:
            form = SolicitudAdopcionForm()

    return render(request, "portal/solicitar_adopcion.html", {"form": form, "mascota": mascota})

