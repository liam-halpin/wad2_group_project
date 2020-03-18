from django.urls import path
from bashmycode import views

from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import redirect

app_name = 'bashmycode'

urlpatterns = [
    path('', views.index, name='index'),
    path('help/', views.help, name='help'),
    path('register/', views.register, name='register'),
    
    path('login/', views.user_login, name='login'),
    path('restricted/', views.restricted, name='restricted'),
    path('logout/', views.user_logout, name='logout'),

    path('bash/', views.bash, name='bash'),
    path('help/', views.help, name='help')
]