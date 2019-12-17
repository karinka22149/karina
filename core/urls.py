from django.urls import path

from .views import *

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', HomeView.as_view(), name='home'),
    path('staff/', StaffView.as_view(), name='staff'),
    path('reciepe/', ReciepeView.as_view(), name='reciepe'),
    path('product/', ProductView.as_view(), name='product')
]
