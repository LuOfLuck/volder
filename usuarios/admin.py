from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Estudiante)
admin.site.register(Profesor)
admin.site.register(Cursoos)
admin.site.register(Materia)
admin.site.register(TipoDeTarea)
admin.site.register(Trabajo)