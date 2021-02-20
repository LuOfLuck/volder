from django.contrib import admin
from noticias.models import SecretarioNoticia, PreceptorNoticia, ProfesorNoticia
# Register your models here.

admin.site.register(SecretarioNoticia)
admin.site.register(PreceptorNoticia)
admin.site.register(ProfesorNoticia)
