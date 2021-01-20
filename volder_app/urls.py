from django.urls import path
from volder_app import views

urlpatterns = [
    path('', views.main, name="home"),
    path('trabajo/<int:id_trabajo>', views.trabajo, name="trabajo"),
    path('materia/<int:id_materia>', views.materia, name="materia"),
]