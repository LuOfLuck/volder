from django.contrib import admin
from .models import *
# Register your models here.
class MateriaAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
class TrabajoAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(Estudiante)
admin.site.register(Profesor)
admin.site.register(Preceptor)
admin.site.register(Cursoos)
admin.site.register(Materia, MateriaAdmin)
admin.site.register(TipoDeTarea)
admin.site.register(Trabajo,TrabajoAdmin)
admin.site.register(Comentario)