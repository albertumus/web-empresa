from django.db import models

# Create your models here.

class Link(models.Model):
    key = models.SlugField(verbose_name="Nombre clase", max_length=100, unique=True)
    name = models.CharField(verbose_name="Red Social", max_length=100) 
    url = models.URLField (verbose_name="Enlace", max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    updated = models.DateTimeField(auto_now=True, verbose_name="Editado")

    class Meta:
            verbose_name = "enlace"
            verbose_name_plural = "enlaces"
            ordering = ["-name"]

    def __str__(self):
        return self.name
