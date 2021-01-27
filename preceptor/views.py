from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from usuarios.models import Preceptor, Cursoos, Estudiante, Materia, Profesor
from volder_app.decorators import RequiredUserAttribute
from django.contrib import messages
import string
import random
# Create your views here.

@RequiredUserAttribute(attribute = 'preceptor', redirect_to_url = '/estudiante/')
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
    


@RequiredUserAttribute(attribute = 'preceptor', redirect_to_url = '/estudiante/')
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


@RequiredUserAttribute(attribute = 'preceptor', redirect_to_url = '/estudiante/')
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
    