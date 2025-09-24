from django.db import models

class Mascota(models.Model):
    nombre = models.CharField(max_length=100)
    especie = models.CharField(max_length=50)
    edad = models.IntegerField()
    ubicacion = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.URLField(blank=True, null=True)  # URL de la foto de la mascota

    def __str__(self):
        return self.nombre


class Solicitante(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        default="Sin dirección"  # Valor por defecto limpio
    )

    def __str__(self):
        return self.nombre


class SolicitudAdopcion(models.Model):
    mensaje = models.TextField()
    fecha_solicitud = models.DateTimeField(auto_now_add=True)
    solicitante = models.ForeignKey(Solicitante, on_delete=models.CASCADE)
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)

    def __str__(self):
        return f"Solicitud de {self.solicitante} para {self.mascota}"
