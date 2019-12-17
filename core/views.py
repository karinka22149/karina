from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views import View

from .models import *
from .forms import *

class LoginView(View):
    '''
    Вьюха авторизации.
    '''
    template_name = 'login.html'
    form_class = LoginForm
    
    def get(self, request, *args, **kwargs):
        '''
        Отображение формы авторизации.
        Если пользователь уже авторизирован, то его отправляет на главную страницу.
        '''
        if request.user.is_authenticated:
            return redirect('home')
        form = self.form_class
        context = {
            'form': form
        }
        return render(request, self.template_name, context)
        
    def post(self, request, *args, **kwargs):
        '''
        Получение данных с формы.
        Сравнивание логина и пароля. Если пользователь найден, то авторизирует его.
        '''
        form = self.form_class(request.POST)
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect('home')
        return redirect('login')

class RegisterView(View):
    '''
    Вьюха регистрации.
    '''
    template_name = 'register.html'
    form_class = RegisterForm
    
    def get(self, request, *args, **kwargs):
        '''
        Отображение формы регистрации.
        Если пользователь авторизирован, то его отправляет на главную страницу.
        '''
        if request.user.is_authenticated:
            return redirect('home')
        form = self.form_class
        context = {
            'form': form
        }
        return render(request, self.template_name, context)
        
    def post(self, request, *args, **kwargs):
        '''
        Получение данных с формы.
        Создается пользователь, авторизирует его. Создает профиль пользователя.
        '''
        user = User.objects.create_user(
            username=request.POST['username'],
            password=request.POST['password'],
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
        )
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        user.email = request.POST['email']
        user.save()
        if user is not None:
            login(request, user)
            return redirect('home')
        return redirect('register')

class LogoutView(View):
    '''
    Вьюха выхода.
    '''
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('login')

class HomeView(View):
    template_name = 'home.html'
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
    def post(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
class StaffView(View):
    template_name = 'staff.html'
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
    def post(self, request, *args, **kwargs):
        return render(request, self.template_name)

class ReciepeView(View):
    template_name = 'reciepe.html'
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
    def post(self, request, *args, **kwargs):
        return render(request, self.template_name)

class ProductView(View):
    template_name = 'product.html'
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
    def post(self, request, *args, **kwargs):
        return render(request, self.template_name)
