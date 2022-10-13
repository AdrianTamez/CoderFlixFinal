from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from AppFinal.models import Avatars

from AppFinal.models import Avatars

class FormularioPeliculas(forms.Form):

    nombre = forms.CharField()
    duracion = forms.IntegerField()

class FormularioCines(forms.Form):

    nombre = forms.CharField()
    ubicacion = forms.CharField()

class UsuarioRegistro(UserCreationForm):

    email = forms.EmailField()
    password1 = forms.CharField(label = "Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label = "Repetir Contraseña", widget=forms.PasswordInput)

    class Meta:

        model = User 
        fields = ["username", "email", "first_name", "password1", "password2"]

class FormularioEditar(UserCreationForm):

    email = forms.EmailField()
    password1 = forms.CharField(label = "Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label = "Repetir Contraseña", widget=forms.PasswordInput)

    class Meta:

        model = User 
        fields = ["email", "first_name", "password1", "password2"]

    
class AvatarFormulario(forms.ModelForm):
    
    class Meta:

        model = Avatars

        fields = ["imagen"]