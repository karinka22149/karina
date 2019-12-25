from django.urls import path

from .views import *

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', HomeView.as_view(), name='home'),
    path('staff/', StaffView.as_view(), name='staff'),
    path('reciepe/', ReciepeView.as_view(), name='reciepe'),
    path('product/', ProductView.as_view(), name='product'),
    
    path('realizationg/',RealizationgView.as_view(),name='realizationg'),
    path('staffg/',StaffgView.as_view(),name='staffg'),
    path('productg/',ProductgView.as_view(),name='productg'),
    path('recipeg/',RecipegView.as_view(),name='recipeg'),
]
