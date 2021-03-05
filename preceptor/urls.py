from django.urls import path
from django.contrib.auth.decorators import login_required
from preceptor import views


urlpatterns = [
    path('', views.main, name="home_preceptor"),
    path('agregar_estudiante/<int:curso>', login_required(views.agregar_estudiante), name="agregar_estudiante"),
    path('agregar_materia/<int:id_curso>', login_required(views.agregar_materia), name="agregar_materia"),
    path('noticias/', login_required(views.noticias_preceptor), name="noticias_preceptor"),
    path('noticia/<int:id_noticia>', login_required(views.ver_noticia_preceptor), name="ver_noticia_preceptor"),
    path('materia/<int:id_materia>', login_required(views.ver_materia_preceptor), name="ver_materia_preceptor"),
    path('trabajo/<int:id_trabajo>', login_required(views.ver_trabajos_preceptor), name="ver_trabajos_preceptor"),
    path('ajustes/', login_required(views.ajustes_preceptor), name="ajustes_preceptor"),
]