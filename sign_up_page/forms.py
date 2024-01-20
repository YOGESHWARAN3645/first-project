from django import forms

class sign_up_form(forms.Form):
    name = forms.CharField(max_length=16)
    username = forms.CharField(max_length=16)
    password =forms.CharField(max_length=16)
    phone_number = forms.IntegerField(max_length=16)
    
