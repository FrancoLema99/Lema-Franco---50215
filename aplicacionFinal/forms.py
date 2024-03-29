from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class RegistroForm(UserCreationForm):

    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={"class":"form-control"}))
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput(attrs={"class":"form-control"}))
    password2 = forms.CharField(label="Confirmar constraseña", widget=forms.PasswordInput(attrs={"class":"form-control"}))

    class Meta:

        model = User
        fields = ["username", "email", "password1", "password2"]


class UserEditForm(UserChangeForm):

    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={"class":"form-control"}))
    first_name = forms.CharField(label="Nombre/s", max_length=50, required=True, widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name = forms.CharField(label="Apellido/s", max_length=50, required=True, widget=forms.TextInput(attrs={"class":"form-control"}))



    class Meta:

        model = User
        fields = ["email", "first_name", "last_name"]

class AvatarForm(forms.Form):

    imagen = forms.ImageField(required=True)