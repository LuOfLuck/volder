from django.shortcuts import render, redirect
from usuarios.models import *

# Create your views here.

def main(request):

    try:
        request.user.estudiante
        ultimos_trabajos = Trabajo.objects.all()
       
        id_curso = request.user.estudiante.curso.id
        materias = Materia.objects.filter(curso=id_curso)
        compañero = Estudiante.objects.filter(curso=id_curso)

        cont = {
            "ultimos_trabajo":ultimos_trabajos,
            "materias":materias,
            "compañero":compañero,
        }
        return render(request, "volder/main.html",cont)
    except:
        return redirect("/profesor/")
    



def trabajo(request, id_trabajo):

    trabajo = Trabajo.objects.get(id=id_trabajo)

    cont = {
    "trabajo":trabajo,
    }

    return render(request, "volder/trabajo.html", cont)

def materia(request, id_materia):
    
    id_curso = request.user.estudiante.curso.id
    compañero = Estudiante.objects.filter(curso=id_curso)

    materia = Materia.objects.get(id=id_materia)
    trabajos = Trabajo.objects.filter(materia = materia)

    cont = {
        "trabajos":trabajos,
        "materia":materia,
        "compañero":compañero,
    }

    return render(request, "volder/materia.html", cont)