from django.shortcuts import render
from usuarios.models import *

# Create your views here.

def main(request):
    if request.user.is_authenticated:

        id_curso = request.user.estudiante.curso.id
        #id_materia = Materia.objects.filter(curso=id_curso)
        ultimos_trabajos = Trabajo.objects.all()

        materias = Materia.objects.filter(curso=id_curso)

        compañero = Estudiante.objects.filter(curso=id_curso)
        cont = {
            "ultimos_trabajo":ultimos_trabajos,
            "materias":materias,
            "compañero":compañero,
        }
    return render(request, "volder/main.html",cont)


def trabajo(request, id_trabajo):
    trabajo = Trabajo.objects.get(id=id_trabajo)
    cont = {
    "trabajo":trabajo,
    }
    return render(request, "volder/trabajo.html", cont)

def materia(request, id_materia):
    materia = Materia.objects.get(id=id_materia)
    trabajos = Trabajo.objects.filter(materia = materia)
    cont = {
    "trabajos":trabajos,
    }
    return render(request, "volder/materia.html", cont)