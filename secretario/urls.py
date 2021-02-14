from django.urls import path
from django.contrib.auth.decorators import login_required
from secretario import views
from django.conf import settings


urlpatterns = [
    path('', login_required(views.main), name="home_secretario"),
    path('agregar_preceptor', login_required(views.agregar_preceptor), name="agregar_preceptor"),
    path('agregar_profesor', login_required(views.agregar_profesor), name="agregar_profesor"),
    path('noticias', login_required(views.noticias), name="noticias"),
]
