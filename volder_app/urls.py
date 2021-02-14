from django.urls import path
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static
from volder_app import views


urlpatterns = [
    path('', login_required(views.main), name="home"),
    path('trabajo/<int:id_trabajo>/', login_required(views.trabajo), name="trabajo"),
    path('materia/<int:id_materia>/', login_required(views.materia), name="materia"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
