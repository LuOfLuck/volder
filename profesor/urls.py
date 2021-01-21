from django.urls import path
from django.contrib.auth.decorators import login_required
from profesor import views


urlpatterns = [
    path('', login_required(views.main), name="home_profesor"),
    path('subir_trabajo/', login_required(views.añadir_trabajo), name="añadir_trabajo"),
    path('ver_trabajo/<int:id_trabajo>', login_required(views.ver_trabajo), name="ver_trabajo"),
]