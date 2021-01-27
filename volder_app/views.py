from django.shortcuts import render, redirect
from usuarios.models import *
from .decorators import *
# Create your views here.
@RequiredUserAttribute(attribute = 'estudiante', redirect_to_url = '/profesor/')
def main(request):
        
        ultimos_trabajos = Trabajo.objects.all().order_by("-fecha_de_subida")
       
        id_curso = request.user.estudiante.curso.id
        materias = Materia.objects.filter(curso=id_curso)
        compañero = Estudiante.objects.filter(curso=id_curso)

        cont = {
            "ultimos_trabajo":ultimos_trabajos,
            "materias":materias,
            "compañero":compañero,
        }
        return render(request, "volder/main.html",cont)



@RequiredUserAttribute(attribute = 'estudiante', redirect_to_url = '/profesor/')
def trabajo(request, id_trabajo):
    trabajo = Trabajo.objects.get(id=id_trabajo)
    if request.user.estudiante.curso != trabajo.materia.curso:
        return redirect("/estudiante/")
    if request.method == "POST":
        comentario = request.POST['comentario']
        coment = Comentario(autor=request.user, comentario=comentario, trabajo=trabajo)
        coment.save()

    
    comentarios = Comentario.objects.filter(trabajo=trabajo)
    cont = {
    "trabajo":trabajo,
    "comentarios":comentarios,
    }

    return render(request, "volder/trabajo.html", cont)


@RequiredUserAttribute(attribute = 'estudiante', redirect_to_url = '/profesor/')
def materia(request, id_materia):
    materia = Materia.objects.get(id=id_materia)
    trabajos = Trabajo.objects.filter(materia = materia)
    if request.user.estudiante.curso != materia.curso:
        return redirect("/estudiante/")


    id_curso = request.user.estudiante.curso.id
    compañero = Estudiante.objects.filter(curso=id_curso)

    cont = {
        "trabajos":trabajos,
        "materia":materia,
        "compañero":compañero,
    }

    return render(request, "volder/materia.html", cont)