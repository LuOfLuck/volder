from django.db import models
from usuarios.models import Cursoos, Materia
from django.contrib.auth.models import User
# Create your models here.

class SecretarioNoticia(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, null=True, blank=True)
    titulo = models.CharField(max_length=25)
    mensaje = models.TextField(max_length=1999)
    url = models.CharField(max_length=200, null=True, blank=True)
    imagen = models.ImageField(upload_to="noticias/secretario", null=True, blank=True)
    created = models.DateField(auto_now_add=True)

    class Meta():
        verbose_name = "Secretario Noticia"
        verbose_name_plural = "Secretario Noticias"

    def __str__(self):
        return self.titulo
class ProfesorNoticia(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, null=True, blank=True)
    titulo = models.CharField(max_length=25)
    mensaje = models.CharField(max_length=1999)
    url = models.CharField(max_length=200, null=True, blank=True)
    imagen = models.ImageField(upload_to="noticias/profesor", null=True, blank=True)
    materia = models.ManyToManyField(Materia)
    created = models.DateField(auto_now_add=True)

    class Meta():
        verbose_name = "Profesor Noticia"
        verbose_name_plural = "Profesores Noticias"

    def __str__(self):
        return self.titulo
