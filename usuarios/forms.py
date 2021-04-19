from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from usuarios.models import Estudiante, Profesor, Preceptor, Secretario

class FormEstudiante(forms.ModelForm):

    class Meta:

        model = Estudiante
        fields = '__all__'

class FormProfesor(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = ['foto']

class FormPreceptor(forms.ModelForm):
    class Meta:
        model = Preceptor
        fields = ['foto']

class FormSecretario(forms.ModelForm):
    class Meta:
        model = Secretario
        fields = ['foto']