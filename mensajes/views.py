from django.shortcuts import render
from django.contrib import messages
from usuarios.models import Secretario, Preceptor, Profesor, Estudiante
from mensajes.models import Grupo_chat, Mensajes
# Create your views here.

def main(request, user):
    try:
         receptor = Estudiante.objects.get(user= user)
    except:
        try:
            receptor = Profesor.objects.get(user= user)
        except:
            try:
                receptor = Preceptor.objects.get(user= user)
            except:
                receptor = Secretario.objects.get(user= user)
                
    try:
        grupo = Grupo_chat.objects.get(persona1=request.user, persona2=receptor.user)
    except:
        try:
            grupo = Grupo_chat.objects.get(persona1=receptor.user, persona2=request.user)
        except:
            grupo = None


    
    if request.method == "POST":
        mensaje = request.POST['mensaje']
        if grupo == None:
            grupo = Grupo_chat(persona1=request.user, persona2=receptor.user)
            grupo.save()

        mensajeEnviado = Mensajes(autor=request.user, mensaje=mensaje, id_conversacion = grupo)
        mensajeEnviado.save()

    if grupo != None:
        mensajes = Mensajes.objects.filter(id_conversacion = grupo)
    else:
        mensajes = []
    print(user)
    print(receptor)
    cont = {
        "receptor":receptor,
        "mensajes":mensajes,
    }
    return render(request, "mensajes/mensajes.html", cont)

def bandeja_de_entrada(request):
    if hasattr(request.user, 'estudiante'):
        extend = "volder/base.html"

    elif hasattr(request.user, 'profesor'):
        extend = "profesor/base.html"

    elif hasattr(request.user, 'preceptor'):   
        extend = "preceptor/base.html"
    else:
        extend = "secretario/base.html"
    grupos = []
    try:
        grupos += Grupo_chat.objects.filter(persona1=request.user)
    except:
        pass
    try:
        grupos += Grupo_chat.objects.filter(persona2=request.user)
    except:
        pass


    if grupos == []:
        messages.success(request, f'Aun no tiene mensajes :(')
    cont = {
        "grupos":grupos,
        "extend":extend,

    }
    return render(request,"mensajes/bandeja_de_entrada.html", cont)