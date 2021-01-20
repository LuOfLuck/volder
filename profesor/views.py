from django.shortcuts import render, redirect
from usuarios.models import *
# Create your views here.

def main(request):
    try:
        request.user.profesor
    except:
        return redirect("/estudiante/")

    return render(request, "profesor/main.html")

def añadir_trabajo(request):

    try:
        request.user.profesor
    except:
        return redirect("/estudiante/")

    return render(request, "profesor/añadir_trabajo.html")
    