from django.db import models
from django.contrib.auth.models import User


class Categoria(models.Model):
    descripcion = models.CharField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.descripcion


class Articulo(models.Model):
    titulo = models.CharField(max_length=120)
    introduccion = models.CharField()
    cuerpo = models.CharField()
    url = models.URLField(null=True, blank=True)
    fecha_publicacion = models.DateField()
    categoria = models.ForeignKey(Categoria)
    created_by = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo