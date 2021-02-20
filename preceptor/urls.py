from django.urls import path
from django.contrib.auth.decorators import login_required
from preceptor import views


urlpatterns = [
    path('', views.main, name="home_preceptor"),
    path('agregar_estudiante/<int:curso>', views.agregar_estudiante, name="agregar_estudiante"),
    path('agregar_materia/<int:id_curso>', views.agregar_materia, name="agregar_materia"),
    path('noticias/', views.noticias_preceptor, name="noticias_preceptor"),
    path('ajustes/', views.ajustes_preceptor, name="ajustes_preceptor"),
]