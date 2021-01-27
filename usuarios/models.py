from django.db import models
from django.contrib.auth.models import User


class Cursoos(models.Model):
    curso = models.CharField(max_length=10, null=True, blank=True)
    division = models.CharField(max_length=10, null=True, blank=True)
    def __str__(self):
        curso_y_division = self.curso + "-" + self.division
        return curso_y_division

class Estudiante(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dni = models.IntegerField(unique=True)
    curso = models.ForeignKey(Cursoos, on_delete = models.CASCADE, null=True, blank=True)
    def __str__(self):
        nombre_y_apellido = self.nombre + " " + self.apellido
        return nombre_y_apellido

class Profesor(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dni = models.IntegerField(unique=True)
    email = models.EmailField(unique=True)
    def __str__(self):
        nombre_y_apellido = self.nombre + " " + self.apellido
        return nombre_y_apellido

class Preceptor(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    cursos = models.ManyToManyField(Cursoos)
    def __str__(self):
        nombre_y_apellido = self.nombre + " " + self.apellido
        return nombre_y_apellido

class Materia(models.Model):
    nombre = models.CharField(max_length=50)
    curso = models.ForeignKey(Cursoos, on_delete = models.CASCADE, null=True, blank=True)
    profesor = models.ForeignKey(Profesor, on_delete = models.CASCADE, null=True, blank=True)
    trabajos_entregados = models.IntegerField(null=True, blank=True)
    def __str__(self):
        nombre_y_curso = self.nombre + " " + str(self.curso)
        return nombre_y_curso

class TipoDeTarea(models.Model):
    tipo = models.CharField(max_length=50)
    def __str__(self):
        return self.tipo

class Trabajo(models.Model):
    titulo = models.CharField(max_length=50)
    materia = models.ForeignKey(Materia, on_delete = models.CASCADE, null=True, blank=True)
    fecha_de_subida = models.DateTimeField(auto_now_add=True)
    fecha_de_entrega = models.DateTimeField(auto_now_add=False)
    tipo_de_trabajo = models.ForeignKey(TipoDeTarea, on_delete = models.CASCADE, null=True, blank=True)
    consigna = models.CharField(max_length=50)
    contenido = models.TextField()
    fuentes = models.CharField(max_length=50)
    def __str__(self):
        return self.titulo
   
class Comentario(models.Model):
    autor = models.ForeignKey(User, on_delete = models.CASCADE)
    comentario = models.CharField(max_length=150)
    trabajo = models.ForeignKey(Trabajo, on_delete = models.CASCADE, null=True, blank=True)
    create = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    def __str__(self):
        return self.comentario