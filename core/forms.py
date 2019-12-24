from django import forms
from django.contrib.auth.models import User
from .models import *

class LoginForm(forms.ModelForm):
    username = forms.CharField(max_length=150, label='Логин')
    password = forms.CharField(widget=forms.PasswordInput, label='Пароль')
    
    class Meta:
        model = User
        fields = ['username', 'password']
        
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

class RegisterForm(forms.ModelForm):
    username = forms.CharField(max_length=50, label='Логин')
    password = forms.CharField(widget=forms.PasswordInput, label='Пароль')

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']
        
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

class RealizationForm(forms.ModelForm):
    
    class Meta:
        model = Realization
        fields = '__all__'

class StaffForm(forms.ModelForm):

    class Meta:
        model = Staff
        fields = '__all__'
