from django import forms
from django.contrib.auth.models import User
from .models import *

class LoginForm(forms.ModelForm):
    username = forms.CharField(max_length=150, label='Логин')
    password = forms.CharField(widget=forms.PasswordInput, label='Пароль')
    
    class Meta:
        model = User
        fields = ['username', 'password']
        
class RegisterForm(forms.ModelForm):
    username = forms.CharField(max_length=50, label='Логин')
    password = forms.CharField(widget=forms.PasswordInput, label='Пароль')
    
    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name']