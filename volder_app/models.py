from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Cursos(models.Model):
    curso = models.CharField(max_length=10, null=True, blank=True)
    division = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        curso_y_division = self.curso + "-" + self.division
        return curso_y_division
