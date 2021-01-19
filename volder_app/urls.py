from django.urls import path
from volder_app import views

urlpatterns = [
    path('', views.main, name="home"),
    path('trabajo/', views.trabajo, name="trabajo"),
]