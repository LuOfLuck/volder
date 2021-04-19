from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from usuarios.models import RespuestaTrabajo

class FormRespuestaTrabajo(forms.ModelForm):

    class Meta:

        model = RespuestaTrabajo
        widgets = {
            'comentario': forms.TextInput(attrs={'placeholder': 'alguna aclaracion'}),
        }
        fields = ['comentario', 'archivo',]