from django.shortcuts import render
from django.contrib.auth.models import User
from volder_app.decorators import RequiredUserAttribute
from django.contrib import messages
from usuarios.models import Profesor, Preceptor, Cursoos, Estudiante, Materia
from noticias.models import SecretarioNoticia, PreceptorNoticia, ProfesorNoticia
from mensajes.models import Grupo_chat
import string
import random

# Create your views here.
@RequiredUserAttribute(attribute = 'secretario', redirect_to_url = '/estudiante/')
def main(request):
    return render(request, "secretario/main.html")
    

@RequiredUserAttribute(attribute = 'secretario', redirect_to_url = '/estudiante/')
def agregar_preceptor(request):
    
    if request.method == "POST":
        try:
            def random_char(y):
                return ''.join(random.choice(string.ascii_letters) for x in range(y))    
            valores = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ<=>@#%.&+"
            password = ""
            usuario = request.POST['nombre'].strip() +   random_char(10)
            password =  password.join([random.choice(valores) for i in range(18)])
            email = request.POST['email']
            user = User.objects.create_user(usuario, email, password)
            user.save()
            nombre = request.POST['nombre']
            apellido = request.POST['apellido']
            dni = request.POST['dni']
            cursos = request.POST.getlist('cursos')
            usuario = User.objects.get(username=usuario)
            preceptor = Preceptor(user=usuario, nombre=nombre, apellido=apellido, dni=dni)
            preceptor.save()
            for cursos in cursos:
                curso = Cursoos.objects.get(id=cursos)
                preceptor.cursos.add(curso)

            messages.success(request, f'usuario {nombre} {apellido} creado')
        except:
            messages.success(request, f'error al crear usuario')
    cursos = Cursoos.objects.all()
    cont ={
        "cursos":cursos
    }
    return render(request, "secretario/agregar_preceptor.html", cont)


@RequiredUserAttribute(attribute = 'secretario', redirect_to_url = '/estudiante/')
def agregar_profesor(request):
 
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
            profesor = Profesor(user=usuario, nombre=nombre, apellido=apellido, dni=dni)
            profesor.save()
            messages.success(request, f'usuario {nombre} {apellido} creado')
        except:
            messages.success(request, f'error al crear usuario')
    return render(request, "secretario/agregar_profesor.html")


@RequiredUserAttribute(attribute = 'secretario', redirect_to_url = '/estudiante/')
def noticias(request):
    if request.method == "POST":
        try:
            titulo = request.POST['titulo']
            mensaje = request.POST['mensaje']
            url = request.POST['url']
            imagen = request.POST['imagen']
            try:
                preceptor = request.POST['preceptor']
            except:
                preceptor = False
            try:
                profesor = request.POST['profesor']
            except:
                profesor = False
            try:
                estudiante = request.POST['estudiante']
            except:
                estudiante = False
            noticia = SecretarioNoticia(user=request.user, titulo=titulo, mensaje=mensaje, url=url, imagen=imagen, preceptor=preceptor, profesor=profesor, estudiante=estudiante)
            noticia.save()

            messages.success(request, f'publicacion completada')
        except:
            messages.success(request, f'error al publicar')

    secretario_noticias = SecretarioNoticia.objects.all()
    preceptor_noticias = PreceptorNoticia.objects.all()
    profesor_noticias = ProfesorNoticia.objects.all()
    cont = {
        "secretario_noticias":secretario_noticias,
        "preceptor_noticias":preceptor_noticias,
        "profesor_noticias":profesor_noticias,
    }   
    return render(request, "secretario/noticias.html", cont)

def ajustes_secretario(request):
    return render(request, "secretario/ajustes_secretario.html")

def secretario_cursos(request):
    cursos = Cursoos.objects.all().order_by("curso")
    return render(request, "secretario/cursos.html", {"cursos":cursos})

def inspeccionar_curso(request, id_curso):
    curso = Cursoos.objects.get(id=id_curso)
    estudiantes = Estudiante.objects.filter(curso=curso)
    materias = Materia.objects.filter(curso=curso)
    preceptores = Preceptor.objects.filter(cursos=curso)
    cont = {
        "curso":curso,
        "estudiantes":estudiantes,
        "materias":materias,
        "preceptores":preceptores,
    }
    return render(request, "secretario/inspeccionar_curso.html", cont)

