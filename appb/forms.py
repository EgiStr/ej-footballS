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
        fields = ["nameD", "nameB", "nickname",
                  "nomorhp", "profil", 'background']


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']


# class SignupForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super(SignupForm, self).__init__(*args, **kwargs)
#         self.fields['nameD'].widget = forms.TextInput(
#             attrs={'placeholder': 'Enter first name'})
#         self.fields['nameB'].widget = forms.TextInput(
#             attrs={'placeholder': 'Enter last name'})

#     nameD = forms.CharField(max_length=100)
#     nameB = forms.CharField(max_length=100)
#     profil = forms.ImageField(help_text="Upload profile image ")

#     class Meta:
#         model = Costumer
#         fields = ('nameD', 'nameB',  'profil', 'user')

#     def signup(self, request, user):
#         # Save your user
#         user.user = request.user
#         user.nameD = self.cleaned_data['nameD']
#         user.nameB = self.cleaned_data['nameB']
#         user.save()
#         user.userprofile.profil = self.cleaned_data.get('profil')
#         user.userprofile.save()
