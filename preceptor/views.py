from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from usuarios.models import Preceptor, Cursoos, Estudiante, Materia, Profesor
from noticias.models import SecretarioNoticia, PreceptorNoticia, ProfesorNoticia
from noticias.forms import FormPreceptorNoticia
from volder_app.decorators import RequiredUserAttribute

import string
import random
# Create your views here.

@RequiredUserAttribute(attribute = 'preceptor', redirect_to_url = '/secretario/')
def main(request):
    preceptor_user = Preceptor.objects.get(user=request.user)

    if request.method == "POST":
        cursosPreceptor = preceptor_user.cursos.filter()
        curso = request.POST['curso']
        estudiantes = Estudiante.objects.filter(curso=curso)
        materias = Materia.objects.filter(curso=curso)
        
    else:
        cursosPreceptor = preceptor_user.cursos.filter()
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

def ajustes_preceptor(request):
    return render(request, "preceptor/ajustes_preceptor.html")