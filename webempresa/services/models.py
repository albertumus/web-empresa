from django.db import models

# Create your models here.

class Service(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titulo")
    subtitle = models.CharField(max_length=200, verbose_name="Subtítulo")
    content = models.TextField(verbose_name="Texto")
    image = models.ImageField(verbose_name = "Imagen", upload_to="services")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    updated = models.DateTimeField(auto_now=True, verbose_name="Editado")

    class Meta:
            verbose_name = "Servicio"
            verbose_name_plural = "Servicios"
            ordering = ["-created"]

    def __str__(self):
        return self.title
