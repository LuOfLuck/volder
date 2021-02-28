from django.db import models
from usuarios.models import Cursoos, Materia
from django.contrib.auth.models import User
# Create your models here.

class SecretarioNoticia(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, null=True, blank=True)
    titulo = models.CharField(max_length=50)
    mensaje = models.TextField(max_length=1999)
    url = models.URLField(max_length=200, null=True, blank=True)
    imagen = models.ImageField(upload_to="noticias/secretario", null=True, blank=True)
    preceptor = models.BooleanField(default=None)
    profesor = models.BooleanField(default=None)
    estudiante = models.BooleanField(default=None)
   
    created = models.DateField(auto_now_add=True)

    class Meta():
        verbose_name = "Secretario Noticia"
        verbose_name_plural = "Secretario Noticias"

    def __str__(self):
        return self.titulo

class PreceptorNoticia(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, null=True, blank=True)
    titulo = models.CharField(max_length=50)
    mensaje = models.CharField(max_length=1999)
    url = models.URLField(max_length=200, null=True, blank=True)
    imagen = models.ImageField(upload_to="noticias/preceptor", null=True, blank=True)
    curso = models.ManyToManyField(Cursoos)
    created = models.DateField(auto_now_add=True)

    class Meta():
        verbose_name = "Preceptor Noticia"
        verbose_name_plural = "Preceptores Noticias"

    def __str__(self):
        return self.titulo

class ProfesorNoticia(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, null=True, blank=True)
    titulo = models.CharField(max_length=50)
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
