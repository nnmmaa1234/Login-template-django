from email.policy import default
import imp
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    email = forms.EmailField()
    class meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']