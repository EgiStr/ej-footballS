from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Costumer
from django import forms


class FormUser(forms.ModelForm):
    """
    docstring
    """
    class Meta:
        model = Costumer
        fields = ["nameD", "nameB", "nickname", "nomorhp", "profil"]


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']
