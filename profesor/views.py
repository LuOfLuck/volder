from django.shortcuts import render, redirect
from usuarios.models import *
from datetime import datetime
from volder_app.decorators import *
from django.contrib import messages
from noticias.models import SecretarioNoticia, PreceptorNoticia, ProfesorNoticia
from usuarios.models import Estudiante
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
@RequiredUserAttribute(attribute = 'profesor', redirect_to_url = '/preceptor/')
def main(request):

    trabajos = Trabajo.objects.all().order_by("-fecha_de_subida")

    for trabajo in trabajos:
        if trabajo.materia.profesor == request.user.profesor:
            ultimo_trabajo = trabajo
            break
    cont = {
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
        try:
            titulo = request.POST['titulo']
            mensaje = request.POST['mensaje']
            url = request.POST['url']
            imagen = request.POST['imagen']
            materias = request.POST.getlist('materia')
            noticia = ProfesorNoticia(user=request.user, titulo=titulo, mensaje=mensaje, imagen=imagen, url=url)
            noticia.save()
            for materia in materias:
                materia = Materia.objects.get(id=materia)
                noticia.materia.add(materia)

        except:
            messages.success(request, f'error al publicar')

    secretario_noticias = SecretarioNoticia.objects.filter(profesor = True).order_by("-created")
    preceptor_noticias = []
    profesor_noticias = ProfesorNoticia.objects.filter(user = request.user).order_by("-created")
    materias = Materia.objects.filter(profesor=request.user.profesor)
    
    
    for materia in materias:
        preceptor_noticias += PreceptorNoticia.objects.filter(curso=materia.curso)
        

    cont = {
        "secretario_noticias":secretario_noticias,
        "preceptor_noticias":preceptor_noticias,
        "profesor_noticias":profesor_noticias,
        "materias":materias,
    }

    return render(request, "profesor/noticias_profesor.html", cont)

@RequiredUserAttribute(attribute = 'profesor', redirect_to_url = '/preceptor/') 
def ajustes_profesor(request):
    return render(request, "profesor/ajustes_profesor.html")

@RequiredUserAttribute(attribute = 'profesor', redirect_to_url = '/preceptor/') 
def materias_profesor(request):
    return render(request, "profesor/materias_profesor.html")