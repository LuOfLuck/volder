from django.shortcuts import render, redirect
from usuarios.models import *
from datetime import datetime
from volder_app.decorators import *
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
        trabajo.save()
        return redirect("/profesor/")

    now = datetime.now()
    materias = Materia.objects.all()
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
    