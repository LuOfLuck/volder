from django.shortcuts import render, redirect
from usuarios.models import *
from datetime import datetime
from volder_app.decorators import *
from django.contrib import messages
from noticias.models import SecretarioNoticia, PreceptorNoticia, ProfesorNoticia, ProfesorNoticiaComentarios
from noticias.forms import FormProfesorNoticia
from usuarios.models import Estudiante
from usuarios.forms import FormProfesor
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
@RequiredUserAttribute(attribute = 'profesor', redirect_to_url = '/preceptor/')
def main(request):

    trabajos = Trabajo.objects.all().order_by("-fecha_de_subida")
    materias = Materia.objects.filter(profesor = request.user.profesor)
    for trabajo in trabajos:
        if trabajo.materia.profesor == request.user.profesor:
            ultimo_trabajo = trabajo
            break
    cont = {
        "materias":materias,
        "trabajos":trabajos,
        "ultimo_trabajo":ultimo_trabajo,
    }
    return render(request, "profesor/main.html", cont)

@RequiredUserAttribute(attribute = 'profesor', redirect_to_url = '/preceptor/')
def añadir_trabajo(request):

    if request.method == "POST":
        titulo = request.POST['titulo']
        materia = Materia.objects.get(id = request.POST['materia'])
        fecha_de_entrega = request.POST['fecha_de_entrega']
        tipo_de_trabajo = TipoDeTarea.objects.get(tipo= request.POST['tipo_de_trabajo'])
        consigna = request.POST['consigna']
        contenido = request.POST['contenido']
        fuentes = request.POST['fuentes']
        trabajo = Trabajo(titulo=titulo, materia=materia, fecha_de_entrega=fecha_de_entrega, tipo_de_trabajo=tipo_de_trabajo, consigna=consigna, contenido=contenido, fuentes=fuentes)
        # trabajo.save()
        estudiantes = Estudiante.objects.filter(curso = materia.curso)
        emailfrom = settings.EMAIL_HOST_USER
        asunto = "NUEVO TRABAJO " + str(tipo_de_trabajo)
        mensaje = f"""
            {tipo_de_trabajo}: {titulo} 
            fecha de entraga:{fecha_de_entrega}
            consigna: {consigna}
            {contenido}             
            fuentes:{fuentes}
            Para ver el trabajo con mayor calidad y poder comunicarte con el profesor y tus compañeros ingresa <a href="volder.online/estudiante/trabajo/{trabajo.id}

        """
        emailrecipiente = ['volderprueba@gmail.com']
        # for estudiante in estudiantes:
        #     emailrecipiente += [estudiante.user.email]
        # print(emailrecipiente)
        send_mail(asunto, mensaje, emailfrom, emailrecipiente)
 
        return redirect("/profesor/")

    now = datetime.now()
    materias = Materia.objects.filter(profesor=request.user.profesor)
    tipo = TipoDeTarea.objects.all()

    
    cont = {
        "materia":materias,
        "tipo":tipo,
        "now":now,
    }
    return render(request, "profesor/añadir_trabajo.html",  cont)

@RequiredUserAttribute(attribute = 'profesor', redirect_to_url = '/preceptor/')   
def ver_trabajo(request,id_trabajo):

    trabajo = Trabajo.objects.get(id=id_trabajo)
    if request.user.profesor != trabajo.materia.profesor:
        return redirect("/profesor/")

    comentarios = Comentario.objects.filter(trabajo=trabajo)
    tipo = TipoDeTarea.objects.all()
    
    if request.method == "POST":        
        try:
            trabajo.titulo = request.POST['titulo']
            trabajo.fecha_de_entrega = request.POST['fecha_de_entrega']
            
            trabajo.tipo_de_trabajo = TipoDeTarea.objects.get(tipo= request.POST['tipo_de_trabajo'])
            trabajo.consigna = request.POST['consigna']
            trabajo.contenido = request.POST['contenido']
            trabajo.fuentes = request.POST['fuentes']
            trabajo.save()
        except:
            comentario = request.POST['comentario']
            coment = Comentario(autor=request.user, comentario=comentario, trabajo=trabajo)
            coment.save()

    cont = {
        "tipo":tipo,
        "trabajo":trabajo,
        "comentarios":comentarios,
    }
    return render(request, "profesor/ver_trabajo.html", cont)

@RequiredUserAttribute(attribute = 'profesor', redirect_to_url = '/preceptor/')   
def grupos(request):
    return render(request, "profesor/grupos.html")

@RequiredUserAttribute(attribute = 'profesor', redirect_to_url = '/preceptor/') 
def trabajo_grupal(request):
    return render(request, "profesor/trabajo_grupal.html")

@RequiredUserAttribute(attribute = 'profesor', redirect_to_url = '/preceptor/') 
def proyecto(request):
    return render(request, "profesor/proyecto.html")

@RequiredUserAttribute(attribute = 'profesor', redirect_to_url = '/preceptor/') 
def gestionar_grupo(request):
    return render(request, "profesor/gestionar_grupo.html")

@RequiredUserAttribute(attribute = 'profesor', redirect_to_url = '/preceptor/') 
def noticias_profesor(request):

    if request.method == "POST":
        form = FormProfesorNoticia(request.POST, request.FILES)
        if form.is_valid():
            model = form.save(commit=False)
            model.user = request.user
            model.save()
            materias = request.POST.getlist('materias')     
            for materia in materias:
                materia = Materia.objects.get(id=materia)            
                model.materia.add(materia)
            messages.success(request, f'Publicacion completa con exito')
        else:
            messages.success(request, f'error al publicar')

    secretario_noticias = SecretarioNoticia.objects.filter(profesor = True).order_by("-created")
    preceptor_noticias = []
    profesor_noticias = ProfesorNoticia.objects.filter(user = request.user).order_by("-created")
    materias = Materia.objects.filter(profesor=request.user.profesor)
    
    
    for materia in materias:
        preceptor_noticias += PreceptorNoticia.objects.filter(curso=materia.curso)
    preceptor_noticias = set(preceptor_noticias)
    formulario = FormProfesorNoticia()

    cont = {
        "secretario_noticias":secretario_noticias,
        "preceptor_noticias":preceptor_noticias,
        "profesor_noticias":profesor_noticias,
        "materias":materias,
        "formulario":formulario,
    }

    return render(request, "profesor/noticias_profesor.html", cont)

@RequiredUserAttribute(attribute = 'profesor', redirect_to_url = '/preceptor/') 
def ajustes_profesor(request):
    if request.method == "POST":
        formulario = FormProfesor(request.POST, request.FILES, instance=request.user.profesor)
        if formulario.is_valid: 
            formulario.save()
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
            

    formulario = FormProfesor(instance=request.user.profesor)
    cont = {
        "formulario":formulario,
    }
    return render(request, "profesor/ajustes_profesor.html", cont)

@RequiredUserAttribute(attribute = 'profesor', redirect_to_url = '/preceptor/') 
def ver_materia(request, id_materia):
    materia = Materia.objects.get(id = id_materia)

    if request.user.profesor != materia.profesor:
        return redirect("/profesor/")
    #protegemos la url

    trabajos = Trabajo.objects.filter(materia = materia)
    noticias = ProfesorNoticia.objects.filter(materia = materia)

    cont = {
        "materia":materia,
        "noticias":noticias,
        "trabajos":trabajos,
    }
    return render(request, "profesor/ver_materia.html", cont)

def ver_noticia_profesor(request, id_noticia):
    noticia = ProfesorNoticia.objects.get(id=id_noticia)
    if noticia.user != request.user:
        return redirect("/profesor/")
    #protegemos la url
    comentarios = ProfesorNoticiaComentarios.objects.filter(noticia=noticia)
    formulario = FormProfesorNoticia(instance=noticia)
    materias = Materia.objects.filter(profesor=request.user.profesor)
    materias_de_noticias = []
    materias_de_noticias += noticia.materia.filter()

    if request.method == "POST":
        formulario =  FormProfesorNoticia(request.POST, request.FILES, instance=noticia)

        if formulario.is_valid():
            instancia = formulario.save(commit=False)
            instancia.user = request.user
            instancia.save()
            materias_recibidas = request.POST.getlist('materias')

            for materias_de_noticia in materias_de_noticias:
                instancia.materia.remove(materias_de_noticia)
            materias_de_noticias = []
            for materia_recibidas in materias_recibidas:           
                materia_recibidas = Materia.objects.get(id=materia_recibidas) 
                materias_de_noticias +=  [materia_recibidas]        
                instancia.materia.add(materia_recibidas)
        else:
            try:
                comentario = request.POST["comentario"]
                nuevo_comentario = ProfesorNoticiaComentarios(user= request.user, mensaje=comentario, noticia=noticia)
                nuevo_comentario.save()
            except:
                print("error")
    
    cont = {
        "noticia":noticia,
        "comentarios":comentarios,
        "formulario":formulario,
        "materias":materias,
        "materias_de_noticias":materias_de_noticias,
    }
    return render(request, "profesor/ver_noticia_profesor.html", cont)