from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from noticias.models import SecretarioNoticia,PreceptorNoticia

class FormSecreatarioNoticia(forms.ModelForm):

    class Meta:

        model = SecretarioNoticia
        widgets = {
            'titulo': forms.TextInput(attrs={'placeholder': 'Titulo...'}),
            'mensaje': forms.Textarea(attrs={'placeholder': '¿en que estas pensando?...'}),
            'url': forms.TextInput(attrs={'placeholder': 'https://www.volder.online'}),
        }
        fields = '__all__'
class FormPreceptorNoticia(forms.ModelForm):

    class Meta:

        model = PreceptorNoticia
        widgets = {
            'titulo': forms.TextInput(attrs={'placeholder': 'Titulo...'}),
            'mensaje': forms.Textarea(attrs={'placeholder': '¿en que estas pensando?...'}),
            'url': forms.TextInput(attrs={'placeholder': 'https://www.volder.online'}),
        }
        fields = '__all__'