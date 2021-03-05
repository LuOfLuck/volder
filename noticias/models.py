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

class SecretarioNoticiaComentarios(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, null=True, blank=True)
    mensaje = models.TextField(max_length=400)
    noticia= models.ForeignKey(SecretarioNoticia, on_delete = models.CASCADE, null=True, blank=True)

    class Meta():
        verbose_name = "Secretario Comenario"
        verbose_name_plural = "Secretarioes Comentarios"

    def __str__(self):
        devuelve = f"{self.user} comento en {self.noticia}: {self.mensaje}"
        return devuelve

class PreceptorNoticia(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, null=True, blank=True)
    titulo = models.CharField(max_length=50)
    mensaje = models.CharField(max_length=1999)
    url = models.URLField(max_length=200, null=True, blank=True)
    imagen = models.ImageField(upload_to="noticias/preceptor", null=True, blank=True)
    curso = models.ManyToManyField(Cursoos, null=True, blank=True)
    created = models.DateField(auto_now_add=True)

    class Meta():
        verbose_name = "Preceptor Noticia"
        verbose_name_plural = "Preceptores Noticias"

    def __str__(self):
        return self.titulo

class PreceptorNoticiaComentarios(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, null=True, blank=True)
    mensaje = models.TextField(max_length=400)
    noticia= models.ForeignKey(PreceptorNoticia, on_delete = models.CASCADE, null=True, blank=True)

    class Meta():
        verbose_name = "Preceptor Comenario"
        verbose_name_plural = "Preceptores Comentarios"

    def __str__(self):
        devuelve = f"{self.user} comento en {self.noticia}: {self.mensaje}"
        return devuelve

class ProfesorNoticia(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, null=True, blank=True)
    titulo = models.CharField(max_length=50)
    mensaje = models.TextField(max_length=1999)
    url = models.URLField(max_length=200, null=True, blank=True)
    imagen = models.ImageField(upload_to="noticias/profesor", null=True, blank=True)
    materia = models.ManyToManyField(Materia, null=True, blank=True)
    created = models.DateField(auto_now_add=True)

    class Meta():
        verbose_name = "Profesor Noticia"
        verbose_name_plural = "Profesores Noticias"

    def __str__(self):
        return self.titulo

class ProfesorNoticiaComentarios(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, null=True, blank=True)
    mensaje = models.TextField(max_length=400)
    noticia= models.ForeignKey(ProfesorNoticia, on_delete = models.CASCADE, null=True, blank=True)

    class Meta():
        verbose_name = "Profesor Comenario"
        verbose_name_plural = "Profesores Comentarios"

    def __str__(self):
        devuelve = f"{self.user} comento en {self.noticia}: {self.mensaje}"
        return devuelve