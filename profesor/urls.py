from django.urls import path
from django.contrib.auth.decorators import login_required
from profesor import views


urlpatterns = [
    path('', login_required(views.main), name="home_profesor"),
    path('subir_trabajo/', login_required(views.añadir_trabajo), name="añadir_trabajo"),
    path('ver_trabajo/<int:id_trabajo>', login_required(views.ver_trabajo), name="ver_trabajo"),
    path('grupos/', login_required(views.grupos), name="grupos"),
    path('trabajo_grupal/', login_required(views.trabajo_grupal), name="trabajo_grupal"),
    path('proyecto/', login_required(views.proyecto), name="proyecto"),
    path('gestionar_grupo/', login_required(views.gestionar_grupo), name="gestionar_grupo"),
    path('noticias_profesor/', login_required(views.noticias_profesor), name="noticias_profesor"),
]