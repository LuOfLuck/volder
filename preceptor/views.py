from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from usuarios.models import Preceptor, Cursoos, Estudiante, Materia, Profesor,Trabajo, Comentario
from noticias.models import SecretarioNoticia, PreceptorNoticia, PreceptorNoticiaComentarios, ProfesorNoticia
from noticias.forms import FormPreceptorNoticia
from volder_app.decorators import RequiredUserAttribute

import string
import random
# Create your views here.

@RequiredUserAttribute(attribute = 'preceptor', redirect_to_url = '/secretario/')
def main(request):
    preceptor_user = Preceptor.objects.get(user=request.user)
    cursosPreceptor = preceptor_user.cursos.filter()
    
    if request.method == "POST":    
        curso = request.POST['curso']
        estudiantes = Estudiante.objects.filter(curso=curso)
        materias = Materia.objects.filter(curso=curso)
    else:
        curso = cursosPreceptor[0].id
        estudiantes = Estudiante.objects.filter(curso=curso)
        materias = Materia.objects.filter(curso=curso)
        
    curso = Cursoos.objects.get(id=curso)
    cont = {
        "cursosPreceptor":cursosPreceptor,
        "estudiantes":estudiantes,
        "materias":materias,
        "curso":curso,
    } 
    return render(request, "preceptor/main.html", cont)
    
@RequiredUserAttribute(attribute = 'preceptor', redirect_to_url = '/secretario/')
def agregar_estudiante(request, curso):
    curso = Cursoos.objects.get(id=curso)
    preceptor_user = Preceptor.objects.get(user=request.user)
    cursosPreceptor = preceptor_user.cursos.filter()

    #validamos si el preceptor no esta modificando la url para dañar la bbdd
    value = False
    for cursos in cursosPreceptor:
        if cursos != curso:
            continue
        else:
            value = True
            break
    if value == False:
         return redirect("/preceptor/")

         
    if request.method == "POST":
        try:
            def random_char(y):
                return ''.join(random.choice(string.ascii_letters) for x in range(y))    
            valores = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ<=>@#%.&+"
            password = ""
            usuario = request.POST['nombre'].strip() + random_char(10)
            password =  password.join([random.choice(valores) for i in range(18)])
            email = request.POST['email']
            user = User.objects.create_user(usuario, email, password)
            user.save()
            nombre = request.POST['nombre']
            apellido = request.POST['apellido']
            dni = request.POST['dni']
            
            usuario = User.objects.get(username = usuario)

            estudiante = Estudiante(user=usuario, nombre=nombre, apellido=apellido, dni=dni, curso=curso)
            estudiante.save()
            messages.success(request, f'usuario {nombre} {apellido} creado')
        except:
            messages.success(request, f'error al crear usuario')

    return render(request, "preceptor/agregar_estudiante.html",{"curso":curso})

@RequiredUserAttribute(attribute = 'preceptor', redirect_to_url = '/secretario/')
def agregar_materia(request,id_curso):
    #validamos si el preceptor no esta modificando la url para dañar la bbdd
    preceptor_user = Preceptor.objects.get(user=request.user)
    cursosPreceptor = preceptor_user.cursos.filter()
    curso = Cursoos.objects.get(id=id_curso)
    value = False
    for cursos in cursosPreceptor:
        if cursos != curso:
            continue
        else:
            value = True
            break
    if value == False:
         return redirect("/preceptor/")
    if request.method == "POST":
        try:
            nombre = request.POST['nombre']
            profesor = Profesor.objects.get(id=request.POST['profesor'])

            materia = Materia(nombre=nombre, curso=curso, profesor=profesor)
            materia.save()
            messages.success(request, f'Profesor {profesor} queda acargo de la materia {nombre}')
        except:
            messages.success(request, f'error al crar materia. Intente de nuevo mas tarde')
       
    profesores= Profesor.objects.all()

    cont = {

        "profesores":profesores,
    }

    return render(request, "preceptor/agregar_materia.html", cont)
@RequiredUserAttribute(attribute = 'preceptor', redirect_to_url = '/secretario/')
def noticias_preceptor(request):


    secretario_noticias = SecretarioNoticia.objects.filter(preceptor = True)
    preceptor_noticias = PreceptorNoticia.objects.filter(user= request.user)
    profesor_noticias = ProfesorNoticia.objects.all()
    profesor_noticia_filtrada = []
    preceptor_user = Preceptor.objects.get(user=request.user)
    preceptor_cursos = preceptor_user.cursos.filter()

    for profesor_noticia in profesor_noticias:
        profesor_noticia_cursos = profesor_noticia.materia.filter()
     
        for profesor_noticia_curso in profesor_noticia_cursos:
            if profesor_noticia_curso.curso ==  preceptor_cursos[0]:
                profesor_noticia_filtrada += [profesor_noticia]
                break

    if request.method == "POST":
        form = FormPreceptorNoticia(request.POST, request.FILES)
        if form.is_valid():
            model = form.save(commit=False)
            model.user = request.user
            model.save()
            cursos = request.POST.getlist('cursos')     
            for curso in cursos:
                curso = Cursoos.objects.get(id=curso)            
                model.curso.add(curso)
            messages.success(request, f'Publicacion completa con exito')
        else:
            messages.success(request, f'algo a salido mal :/')


    formualario = FormPreceptorNoticia()
    cont = {
        "secretario_noticias":secretario_noticias,
        "preceptor_noticias":preceptor_noticias,
        "profesor_noticia_filtrada":profesor_noticia_filtrada,
        "preceptor_cursos":preceptor_cursos,
        "formulario":formualario,

    }
    return render(request, "preceptor/noticias_preceptor.html", cont)

@RequiredUserAttribute(attribute = 'preceptor', redirect_to_url = '/secretario/')
def ver_noticia_preceptor(request, id_noticia):
    noticia = PreceptorNoticia.objects.get(id=id_noticia)
    if noticia.user != request.user:
        return redirect("/profesor/")
    #protegemos la url
    formulario = FormPreceptorNoticia(instance=noticia)
    cursos_de_noticias = noticia.curso.filter()
    if request.method == "POST":
        # Actualizamos el formulario con los datos recibidos
        formulario =  FormPreceptorNoticia(request.POST, request.FILES, instance=noticia)
        # Si el formulario es válido...
        if formulario.is_valid():
            instancia = formulario.save(commit=False)
            # Podemos guardarla cuando queramos
            instancia.user = request.user
            instancia.save()
            cursos_recibios = request.POST.getlist('cursos')
            

            for cursos_de_noticia in cursos_de_noticias:
                instancia.curso.remove(cursos_de_noticia)

            cursos_de_noticias = []
            for curso_recibido in cursos_recibios:           
                curso_recibido = Cursoos.objects.get(id=curso_recibido) 
                cursos_de_noticias +=  [curso_recibido]        
                instancia.curso.add(curso_recibido)
        else:
            try:
                comentario = request.POST["comentario"]
                nuevo_comentario = PreceptorNoticiaComentarios(user= request.user, mensaje=comentario, noticia=noticia)
                nuevo_comentario.save()
            except:
                print("error")
    
    comentarios = PreceptorNoticiaComentarios.objects.filter(noticia=noticia)
    cursos = request.user.preceptor.cursos.filter()
    cont = {
        "cursos":cursos,
        "noticia":noticia,
        "comentarios":comentarios,
        "formulario":formulario,
        "cursos_de_noticias":cursos_de_noticias,
        
    }
    return render(request, "preceptor/ver_noticia_preceptor.html",cont)

def ver_materia_preceptor(request, id_materia):
    if hasattr(request.user, 'preceptor'):
        extend = "preceptor/base.html"
    elif hasattr(request.user, 'secretario'):
        extend = "secretario/base.html"
    else:
        return redirect("/estudiante/")

    materia = Materia.objects.get(id=id_materia)
    trabajos = Trabajo.objects.filter(materia=materia)
    noticias = ProfesorNoticia.objects.filter(materia=materia)

    cont = {
        "materia":materia,
        "trabajos":trabajos,
        "noticias":noticias,
        "extend":extend,
    }

    return render(request, "preceptor/ver_materia_preceptor.html",cont) 

def ver_trabajos_preceptor(request, id_trabajo):
    if hasattr(request.user, 'preceptor'):
        extend = "preceptor/base.html"
    elif hasattr(request.user, 'secretario'):
        extend = "secretario/base.html"
    else:
        return redirect("/estudiante/")
    trabajo = Trabajo.objects.get(id=id_trabajo)

    if request.method == "POST":
        comentario = request.POST["comentario"]
        nuevo_comentario = Comentario(autor=request.user, comentario=comentario, trabajo=trabajo)
        nuevo_comentario.save()
    comentarios = Comentario.objects.filter(trabajo = trabajo)

    cont = {
        "trabajo":trabajo,
        "comentarios":comentarios,
        "extend":extend,
    }
    return render(request, "preceptor/ver_trabajos_preceptor.html",cont)

@RequiredUserAttribute(attribute = 'preceptor', redirect_to_url = '/secretario/')
def ajustes_preceptor(request):
    return render(request, "preceptor/ajustes_preceptor.html")