from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Grupo_chat(models.Model):
    persona1 = models.ForeignKey(User, on_delete = models.CASCADE,related_name='persona1')
    persona2 = models.ForeignKey(User, on_delete = models.CASCADE,related_name='persona2')

    def __str__(self):
        vuelta = f" charla entre {self.persona1} y {self.persona2}"
        return vuelta

class Mensajes(models.Model):
    autor = models.ForeignKey(User, on_delete = models.CASCADE, null=True, blank=True)
    id_conversacion = models.ForeignKey(Grupo_chat, on_delete = models.CASCADE)
    mensaje = models.TextField(max_length=1000)

    def __str__(self):
        return self.mensaje
