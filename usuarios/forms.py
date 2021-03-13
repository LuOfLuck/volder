from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from usuarios.models import Estudiante

class FormEstudiante(forms.ModelForm):

    class Meta:

        model = Estudiante
        # widgets = {
        #     'titulo': forms.TextInput(attrs={'placeholder': 'Titulo'}),
        #     'mensaje': forms.Textarea(attrs={'placeholder': '¿en que estas pensando?...'}),
        #     'url': forms.TextInput(attrs={'placeholder': 'https://www.volder.online'}),
        # }
        fields = '__all__'