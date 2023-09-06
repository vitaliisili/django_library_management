from django.contrib.auth.forms import UserCreationForm
from django import forms

from apps.user.models import User


class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    password2 = forms.CharField(label='Password Confirmation')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
