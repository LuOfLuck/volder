from django.shortcuts import render, redirect
from usuarios.models import *
from usuarios.forms import FormEstudiante
from volder_app.forms import FormRespuestaTrabajo
from noticias.models import SecretarioNoticia, PreceptorNoticia, ProfesorNoticia
from volder_app.decorators import *
# Create your views here.
@RequiredUserAttribute(attribute = 'estudiante', redirect_to_url = '/profesor/')
def main(request):
        todos_los_trabajos = Trabajo.objects.all()
        trabajos = Trabajo.objects.filter(materia__curso= request.user.estudiante.curso)


        materias = Materia.objects.filter(curso=request.user.estudiante.curso.id)
        compañero = Estudiante.objects.filter(curso=request.user.estudiante.curso.id)
        nota = []
        respuesta = None
        total_respestas = []
        for trabajo in trabajos:
            try:
                respuesta = RespuestaTrabajo.objects.get(trabajo=trabajo, estudiante=request.user.estudiante)
                total_respestas.append(respuesta)
            except:
                respuesta = None
            try:
                nota.append(NotaTrabajo.objects.get(respuestaTrabajo=respuesta))
            except:
                pass
        cont = {
            "trabajos":trabajos,
            "materias":materias,
            "compañero":compañero,
            "notas":nota,
            "total_respestas":total_respestas,
        }
        return render(request, "volder/main.html",cont)



@RequiredUserAttribute(attribute = 'estudiante', redirect_to_url = '/profesor/')
def trabajo(request, id_trabajo):

    trabajo = Trabajo.objects.get(id=id_trabajo)
    if request.user.estudiante.curso != trabajo.materia.curso:
        return redirect("/estudiante/")
    if request.method == "POST":
        form = FormRespuestaTrabajo(request.POST, request.FILES)
        if form.is_valid:
            form_save = form.save(commit=False)
            form_save.estudiante = request.user.estudiante
            form_save.trabajo = trabajo
            form_save.save()
        else:
            comentario = request.POST['comentario']
            coment = Comentario(autor=request.user, comentario=comentario, trabajo=trabajo)
            coment.save()

    try:
        respuesta_trabajo = RespuestaTrabajo.objects.get(estudiante=request.user.estudiante, trabajo=trabajo)
    except:
        respuesta_trabajo = None
    
    if(respuesta_trabajo):
        try:
            nota = NotaTrabajo.objects.get(respuestaTrabajo = respuesta_trabajo)
        except:
            nota = None
        form = None
    else:
        nota = None
        form = FormRespuestaTrabajo()

    comentarios = Comentario.objects.filter(trabajo=trabajo)
    cont = {
    "trabajo":trabajo,
    "comentarios":comentarios,
    "form":form,
    "nota":nota,
    }

    return render(request, "volder/trabajo.html", cont)


@RequiredUserAttribute(attribute = 'estudiante', redirect_to_url = '/profesor/')
def materia(request, id_materia):

    materia = Materia.objects.get(id=id_materia)
    trabajos = Trabajo.objects.filter(materia = materia)
    if request.user.estudiante.curso != materia.curso:
        return redirect("/estudiante/")

    nota = []
    respuesta = None
    for trabajo in trabajos:
        try:
            respuesta = RespuestaTrabajo.objects.get(trabajo=trabajo, estudiante=request.user.estudiante)
            print(respuesta)
        except:
            respuesta = None
        try:
            nota += [NotaTrabajo.objects.get(respuestaTrabajo=respuesta)]
        except:
            pass

    id_curso = request.user.estudiante.curso.id
    compañero = Estudiante.objects.filter(curso=id_curso)

    cont = {
        "trabajos":trabajos,
        "materia":materia,
        "compañero":compañero,
        "notas":nota,
    }

    return render(request, "volder/materia.html", cont)

@RequiredUserAttribute(attribute = 'estudiante', redirect_to_url = '/profesor/')
def noticias_estudiante(request):
    secretario_noticias = SecretarioNoticia.objects.all()
    preceptor_noticias = PreceptorNoticia.objects.filter(curso = request.user.estudiante.curso)
    profesor_noticias_defaul = ProfesorNoticia.objects.all()
    profesor_noticias = []
    for noticia in profesor_noticias_defaul:
        noticia_cursos = noticia.materia.filter()
        for noticia_curso in noticia_cursos:
            if noticia_curso.curso == request.user.estudiante.curso:
                profesor_noticias += [noticia]
                break
       

    cont = {
       
        "secretario_noticias":secretario_noticias,
        "preceptor_noticias":preceptor_noticias,
        "profesor_noticias":profesor_noticias,
    }
    return render (request, "volder/noticias_estudiante.html",cont)

def ajustes_estudiante(request):


    if request.method == "POST":
        formulario =  FormEstudiante(request.POST, request.FILES, instance=request.user.estudiante)
        if formulario.is_valid():
            instancia = formulario.save(commit=False)
            # Podemos guardarla cuando queramos
            instancia.user = request.user
            instancia.curso = request.user.estudiante.curso
            instancia.dni = request.user.estudiante.dni
            instancia.save()
            try:
                user = request.user
                username = request.POST["username_new"]

                if len(username) > 7:
                    user.username = username

                email = request.POST["email"]
                if ("@" in email) and ("." in email):
                    user.email = email
                user.save()
            except:
                pass
        else:
            print("error")
    formulario = FormEstudiante(instance=request.user.estudiante)


    cont = {
        "formulario":formulario,
    }
    return render (request, "volder/ajustes_estudiante.html", cont)