from django.db import models
from django.contrib.auth.models import User


class Cursoos(models.Model):
    curso = models.CharField(max_length=10, null=True, blank=True)
    division = models.CharField(max_length=10, null=True, blank=True)
    class Meta():
        ordering = ['curso']
    def __str__(self):
        curso_y_division = self.curso + "-" + self.division
        return curso_y_division
 
    @property
    def total_estudiantes(self):
        estudiantes = self.estudiante_set.all()
        total_estudiantes = sum([1 for estudiante in estudiantes])
        return total_estudiantes
    def total_materias(self):
        materias = self.materia_set.all()
        total_materias = sum([1 for materia in materias])
        return total_materias

class Estudiante(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dni = models.IntegerField(unique=True)
    curso = models.ForeignKey(Cursoos, on_delete = models.CASCADE, null=True, blank=True)
    foto =  models.ImageField(upload_to="fotos_de_perfil/estudiante", null=True, blank=True)

    class Meta():
        ordering = ['apellido']

    def __str__(self):
        nombre_y_apellido = self.nombre + " " + self.apellido
        return nombre_y_apellido
    @property
    def imageURL(self):
        try:
            url = self.foto.url
        except:
            url = "/static/img/fotoPerfil.jpg"
        return url

class Profesor(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dni = models.IntegerField(unique=True)
    foto =  models.ImageField(upload_to="fotos_de_perfil/profesor", null=True, blank=True)

    class Meta():
        ordering = ['apellido']

    def __str__(self):
        nombre_y_apellido = self.nombre + " " + self.apellido
        return nombre_y_apellido
    @property
    def imageURL(self):
        try:
            url = self.foto.url
        except:
            url = "/static/img/fotoPerfil.jpg"
        return url

class Preceptor(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    cursos = models.ManyToManyField(Cursoos, null=True, blank=True)
    dni = models.IntegerField(unique=True, null=True, blank=True)
    foto =  models.ImageField(upload_to="fotos_de_perfil/preceptor", null=True, blank=True)
    class Meta():
        ordering = ['apellido']
    def __str__(self):
        nombre_y_apellido = self.nombre + " " + self.apellido
        return nombre_y_apellido
    @property
    def imageURL(self):
        try:
            url = self.foto.url
        except:
            url = "/static/img/fotoPerfil.jpg"
        return url

class Secretario(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    foto =  models.ImageField(upload_to="fotos_de_perfil/secretario", null=True, blank=True)
    def __str__(self):
        nombre_y_apellido = self.nombre + " " + self.apellido
        return nombre_y_apellido
    @property
    def imageURL(self):
        try:
            url = self.foto.url
        except:
            url = "/static/img/fotoPerfil.jpg"
        return url

    def total_preceptores(self):
        preceptores = Preceptor.objects.all()
        total_preceptores = sum([1 for preceptor in preceptores])
        return total_preceptores

    def total_cursos(self):
        cursos = Cursoos.objects.all()
        total_cursos = sum([1 for curso in cursos])
        return total_cursos

    def total_profesores(self):
        profesores = Profesor.objects.all()
        total_profesores = sum([1 for profesor in profesores])
        return total_profesores

    def total_estudiantes(self):
        estudiantes = Estudiante.objects.all()
        total_estudiantes = sum([1 for estudiante in estudiantes])
        return total_estudiantes

class Materia(models.Model):
    nombre = models.CharField(max_length=50)
    curso = models.ForeignKey(Cursoos, on_delete = models.CASCADE, null=True, blank=True)
    profesor = models.ForeignKey(Profesor, on_delete = models.CASCADE, null=True, blank=True)
    trabajos_entregados = models.IntegerField(null=True, blank=True)
    class Meta():
        ordering = ['nombre']
    def __str__(self):
        nombre_y_curso = self.nombre + " " + str(self.curso)
        return nombre_y_curso
    @property
    def total_trabajos(self):
        trabajos = self.trabajo_set.all()
        total_trabajos = sum([1 for trabajo in trabajos])
        return total_trabajos


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
    class Meta():
        ordering = ['-fecha_de_subida']
        
    def __str__(self):
        return self.titulo
   
class Comentario(models.Model):
    autor = models.ForeignKey(User, on_delete = models.CASCADE)
    comentario = models.CharField(max_length=150)
    trabajo = models.ForeignKey(Trabajo, on_delete = models.CASCADE, null=True, blank=True)
    create = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    def __str__(self):
        return self.comentario

class RespuestaTrabajo(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete = models.CASCADE)
    comentario = models.CharField(max_length = 400, null=True, blank=True)
    archivo = models.FileField(upload_to='respuestas-trabajo/%Y/%m/%d/')
    trabajo = models.ForeignKey(Trabajo, on_delete = models.CASCADE)
    create = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    def __str__(self):
        return str(self.estudiante) + str(self.comentario) 

class NotaTrabajo(models.Model):
    estadoNota = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10')
    )
    respuestaTrabajo = models.ForeignKey(RespuestaTrabajo, on_delete = models.CASCADE)
    comentario = models.TextField(max_length=200, null=True, blank=True)
    nota = models.CharField(max_length=20, choices=estadoNota)
    def __str__(self):
        return str(self.respuestaTrabajo) + " " + str(self.nota) 


