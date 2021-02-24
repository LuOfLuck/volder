from django.urls import path
from django.contrib.auth.decorators import login_required
from mensajes import views


urlpatterns = [
    path('<int:user>', views.main, name="mensajes"),
    path('bandeja_de_entrada', views.bandeja_de_entrada, name="bandeja_de_entrada"),
]