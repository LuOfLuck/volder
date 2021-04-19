from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from usuarios.models import NotaTrabajo

class FormNota(forms.ModelForm):

    class Meta:

        model = NotaTrabajo
        widgets = {
            'comentario': forms.TextInput(attrs={'placeholder': 'alguna aclaración'}),
        }
        fields = ['comentario', 'nota']