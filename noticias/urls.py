from django.urls import path
from django.contrib.auth.decorators import login_required
from noticias import views


urlpatterns = [
    path('profesor/<int:id_noticia>', views.ver_noticia_p, name="ver_noticia_p"),
    path('preceptor/<int:id_noticia>', views.ver_noticia_prece, name="ver_noticia_prece"),
    path('secretario/<int:id_noticia>', views.ver_noticia_secre, name="ver_noticia_secre"),
]