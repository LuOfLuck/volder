from django.urls import path
from django.contrib.auth.decorators import login_required
from volder_app import views


urlpatterns = [
    path('', login_required(views.main), name="home"),
    path('trabajo/<int:id_trabajo>/', login_required(views.trabajo), name="trabajo"),
    path('materia/<int:id_materia>/', login_required(views.materia), name="materia"),
]