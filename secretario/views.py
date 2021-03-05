from django.shortcuts import render
from django.contrib.auth.models import User
from volder_app.decorators import RequiredUserAttribute
from django.contrib import messages
from django.forms import modelformset_factory
from usuarios.models import Profesor, Preceptor, Cursoos, Estudiante, Materia
from noticias.models import SecretarioNoticia, SecretarioNoticiaComentarios, PreceptorNoticia, ProfesorNoticia
from mensajes.models import Grupo_chat
from noticias.forms import FormSecreatarioNoticia
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
        form = FormSecreatarioNoticia(request.POST, request.FILES)
        if form.is_valid():
            try:
                model = form.save(commit=False)
                model.user = request.user
                model.save()
                messages.success(request, f'publicacion completada')
            except:
                messages.success(request, f'error al publicar')

    secretario_noticias = SecretarioNoticia.objects.all()
    preceptor_noticias = PreceptorNoticia.objects.all()
    profesor_noticias = ProfesorNoticia.objects.all()
    formulario = FormSecreatarioNoticia()
    cont = {
        "secretario_noticias":secretario_noticias,
        "preceptor_noticias":preceptor_noticias,
        "profesor_noticias":profesor_noticias,
        "formulario":formulario,
    }   
    return render(request, "secretario/noticias.html", cont)

def ver_noticia_secretario(request, id_noticia):
    noticia = SecretarioNoticia.objects.get(id=id_noticia)
    comentarios = SecretarioNoticiaComentarios.objects.filter(noticia=noticia)
    formulario = FormSecreatarioNoticia(instance=noticia)
    if request.method == "POST":
        # Actualizamos el formulario con los datos recibidos
        formulario =   FormSecreatarioNoticia(request.POST, request.FILES, instance=noticia)
        # Si el formulario es válido...
        if formulario.is_valid():
            instancia = formulario.save(commit=False)
            # Podemos guardarla cuando queramos
            instancia.user = request.user
            instancia.save()
            
    cont = {
        "noticia":noticia,
        "comentarios":comentarios,
        "formulario":formulario,
    }
    return render(request, "secretario/ver_noticia_secretario.html", cont)

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

