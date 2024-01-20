# forms.py
from django import forms
from .models import members

class UserLoginForm(forms.ModelForm):
    model = User
    fields = ['username', 'password']
