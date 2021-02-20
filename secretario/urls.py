from django.urls import path
from django.contrib.auth.decorators import login_required
from secretario import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', login_required(views.main), name="home_secretario"),
    path('agregar_preceptor', login_required(views.agregar_preceptor), name="agregar_preceptor"),
    path('agregar_profesor', login_required(views.agregar_profesor), name="agregar_profesor"),
    path('noticias', login_required(views.noticias), name="noticias"),
    path('ajustes', login_required(views.ajustes_secretario), name="ajustes_secretario"),
    path('cursos', login_required(views.secretario_cursos), name="secretario_cursos"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
