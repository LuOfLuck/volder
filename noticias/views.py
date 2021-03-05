from django.shortcuts import render
from noticias.models import SecretarioNoticia, SecretarioNoticiaComentarios, PreceptorNoticia, PreceptorNoticiaComentarios, ProfesorNoticia, ProfesorNoticiaComentarios
# Create your views here.

def comprobar_usar(user):
    if hasattr(user, 'estudiante'):
        extend = "volder/base.html"
    elif hasattr(user, 'profesor'):
        extend = "profesor/base.html"
    elif hasattr(user, 'preceptor'):   
        extend = "preceptor/base.html"
    else:
        extend = "secretario/base.html"
    return extend


def ver_noticia_p(request, id_noticia):
    user = request.user
    extend= comprobar_usar(user)
    noticia = ProfesorNoticia.objects.get(id = id_noticia)
    if request.method == "POST":
        comentario = request.POST["comentario"]
        guardar_comentario = ProfesorNoticiaComentarios(user=request.user, mensaje=comentario, noticia=noticia)
        guardar_comentario.save()

    comentarios = ProfesorNoticiaComentarios.objects.filter(noticia = noticia)
    
    cont = {
        "extend":extend,
        "noticia":noticia,
        "comentarios":comentarios,
    }
    return render (request, "noticias/noticias_y_comentarios.html", cont)

def ver_noticia_prece(request, id_noticia):
   
    user = request.user
    extend= comprobar_usar(user)
    noticia = PreceptorNoticia.objects.get(id = id_noticia)

    if request.method == "POST":
        comentario = request.POST["comentario"]
        guardar_comentario = PreceptorNoticiaComentarios(user=request.user, mensaje=comentario, noticia=noticia)
        guardar_comentario.save()

    comentarios = PreceptorNoticiaComentarios.objects.filter(noticia = noticia)
    cont = {
        "extend":extend,
        "noticia":noticia,
        "comentarios":comentarios,
    }
    return render (request, "noticias/noticias_y_comentarios.html", cont)

def ver_noticia_secre(request, id_noticia):
    user = request.user
    extend= comprobar_usar(user)
    noticia = SecretarioNoticia.objects.get(id = id_noticia)
    if request.method == "POST":
        comentario = request.POST["comentario"]
        guardar_comentario = SecretarioNoticiaComentarios(user=request.user, mensaje=comentario, noticia=noticia)
        guardar_comentario.save()
    comentarios = SecretarioNoticiaComentarios.objects.filter(noticia = noticia)
    cont = {
        "extend":extend,
        "noticia":noticia,
        "comentarios":comentarios,
    }
    return render (request, "noticias/noticias_y_comentarios.html", cont)