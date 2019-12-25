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
    form_class = RealizationForm
    
    def get(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            return redirect('login')
        form = self.form_class
        realization = Realization.objects.all()
        context = {
            'form': form,
            'realization': realization
        }
        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        realization = Realization.objects.all()
        if form.is_valid():
            form.save()
        context = {
            'form': form,
            'realization': realization
        }
        return render(request, self.template_name, context)

class StaffView(View):
    template_name = 'staff.html'
    form_class = StaffForm
    
    def get(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            return redirect('login')
        form = self.form_class
        staff = Staff.objects.all()
        context = {
            'form': form,
            'staff' : staff
        }
        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        staff = Staff.objects.all()
        if form.is_valid():
            form.save()
        context = {
            'form': form,
            'staff' : staff
        }
        return render(request, self.template_name,context)

class ReciepeView(View):
    template_name = 'reciepe.html'
    form_class = ReciepeForm
    
    def get(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            return redirect('login')
        form = self.form_class
        recipe = Recipe.objects.all()
        context = {
            'form': form,
            'recipe' : recipe
        }
        return render(request, self.template_name,context)
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
        context = {
            'form': form,
        }
        return render(request, self.template_name)

class ProductView(View):
    template_name = 'product.html'
    form_class = ProductForm
    
    def get(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            return redirect('login')
        form = self.form_class
        product = Product.objects.all()
        context = {
            'form': form,
            'product' : product
        }
        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
        context = {
            'form': form,
        }
        return render(request, self.template_name)

class RealizationgView(View):
    template_name = 'realizationg.html'
    form_class = RealizationgForm
    
    def get(self, request, *args, **kwargs):
        form = self.form_class
        realization = Realization.objects.all()
        context = {
            'form': form,
            'realization': realization
        }
        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
        context = {
            'form': form
        }
        return render(request, self.template_name, context)

class StaffgView(View):
    template_name = 'staffg.html'
    form_class = StaffForm
    
    def get(self, request, *args, **kwargs):
        form = self.form_class
        staff = Staff.objects.all()
        context = {
            'form': form,
            'staff' : staff
        }
        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        staff = Staff.objects.all()
        if form.is_valid():
            form.save()
        context = {
            'form': form,
            'staff' : staff
        }
        return render(request, self.template_name,context)

class RecipegView(View):
    template_name = 'recipeg.html'
    form_class = ReciepeForm
    
    def get(self, request, *args, **kwargs):
        form = self.form_class
        recipe = Recipe.objects.all()
        context = {
            'form': form,
            'recipe' : recipe
        }
        return render(request, self.template_name,context)
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
        context = {
            'form': form,
        }
        return render(request, self.template_name)

class ProductgView(View):
    template_name = 'productg.html'
    form_class = ProductForm
    
    def get(self, request, *args, **kwargs):
        form = self.form_class
        product = Product.objects.all()
        context = {
            'form': form,
            'product' : product
        }
        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
        context = {
            'form': form,
        }
        return render(request, self.template_name)


