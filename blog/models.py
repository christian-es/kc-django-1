from django.db import models
from django.contrib.auth.models import User


class Categoria(models.Model):
    descripcion = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.descripcion


class Articulo(models.Model):
    titulo = models.CharField(max_length=100)
    introduccion = models.CharField(max_length=150)
    cuerpo = models.TextField()
    url = models.URLField(null=True, blank=True)
    fecha_publicacion = models.DateField()
    categoria = models.ForeignKey(Categoria)
    created_by = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo