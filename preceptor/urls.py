from django.urls import path
from django.contrib.auth.decorators import login_required
from preceptor import views


urlpatterns = [
    path('', views.main, name="home_preceptor"),
    path('agregar_estudiante/<int:curso>', login_required(views.agregar_estudiante), name="agregar_estudiante"),
    path('agregar_materia/<int:id_curso>', login_required(views.agregar_materia), name="agregar_materia"),
    path('noticias/', login_required(views.noticias_preceptor), name="noticias_preceptor"),
    path('ajustes/', login_required(views.ajustes_preceptor), name="ajustes_preceptor"),
]