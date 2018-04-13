from django import forms
from django.forms import ModelForm

from django.contrib.auth.forms import UserCreationForm
from .models import Customer



class LoginForm(forms.Form):
   username = forms.CharField(max_length = 100)
   password = forms.CharField(widget = forms.PasswordInput())


class SignUpForm(ModelForm):
    name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    password = forms.CharField(widget = forms.PasswordInput())    
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = Customer
        fields = ('name', 'password', 'email', 'created_date')