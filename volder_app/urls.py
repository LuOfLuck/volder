from django.urls import path
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static
from volder_app import views


urlpatterns = [
    path('', login_required(views.main), name="home"),
    path('trabajo/<int:id_trabajo>/', login_required(views.trabajo), name="trabajo"),
    path('materia/<int:id_materia>/', login_required(views.materia), name="materia"),
    path('noticias/', login_required(views.noticias_estudiante), name="noticias_estudiante"),
    path('ajustes/', login_required(views.ajustes_estudiante), name="ajustes_estudiante"),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
