from django.forms import ModelForm
from user.models import profile, login
from django import forms
class RegistrationForm(ModelForm):
    password = forms.CharField(widget = forms.PasswordInput)
    class Meta:
        model = profile
        fields = ('username', 'email', 'password', 'mobilenumber')

class LoginForm(ModelForm):
    Password = forms.CharField(widget = forms.PasswordInput)
    class Meta:
        model = login
        fields = ('username', 'Password')
    

