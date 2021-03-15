from django.urls import path
from django.contrib.auth.decorators import login_required
from secretario import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', login_required(views.main), name="home_secretario"),
    path('agregar_preceptor', login_required(views.agregar_preceptor), name="agregar_preceptor"),
    path('ver_preceptores/', login_required(views.ver_preceptores), name="ver_preceptores"),
    path('agregar_profesor', login_required(views.agregar_profesor), name="agregar_profesor"),
    path('ver_profesores/', login_required(views.ver_profesores), name="ver_profesores"),
    path('ver_estudiantes/', login_required(views.ver_estudiantes), name="ver_estudiantes"),
    path('noticias/', login_required(views.noticias), name="noticias"),
    path('ajustes/', login_required(views.ajustes_secretario), name="ajustes_secretario"),
    path('cursos/', login_required(views.secretario_cursos), name="secretario_cursos"),
    path('inspeccionar_curso/<int:id_curso>/', login_required(views.inspeccionar_curso), name="inspeccionar_curso"),
    path('ver_noticia/<int:id_noticia>/', login_required(views.ver_noticia_secretario), name="ver_noticia_secretario"),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
