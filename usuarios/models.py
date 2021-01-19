from django.db import models
from django.contrib.auth.models import User
from volder_app.models import Cursos
class Estudiante(models.Model):

    user = models.OneToOneField(User, on_delete = models.CASCADE)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dni = models.IntegerField(unique=True)
    email = models.EmailField(unique=True)
    curso = models.ForeignKey(Cursos, on_delete = models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.nombre
