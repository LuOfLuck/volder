from django.shortcuts import render
from django.contrib.auth.models import User
from volder_app.decorators import RequiredUserAttribute
from django.contrib import messages
from usuarios.models import Profesor, Preceptor, Cursoos
from noticias.models import SecretarioNoticia
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
            usuario = request.POST['nombre'].strip() + random_char(10)
            password =  password.join([random.choice(valores) for i in range(18)])
            email = request.POST['email']
            user = User.objects.create_user(usuario, email, password)
            user.save()
            nombre = request.POST['nombre']
            apellido = request.POST['apellido']
            dni = request.POST['dni']
            cursos = request.POST.getlist('cursos')
            print(cursos)
            usuario = User.objects.get(username=usuario)
            print(usuario)
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
            noticia = SecretarioNoticia(user=request.user, titulo=titulo, mensaje=mensaje, url=url, imagen=imagen)
            noticia.save()
            messages.success(request, f'publicacion completada')
        except:
            messages.success(request, f'error al publicar')

    noticias = SecretarioNoticia.objects.all()
    cont = {
        "noticias":noticias
    }   
    return render(request, "secretario/noticias.html", cont)