from django.urls import path
from bashmycode import views

app_name = 'bashmycode'

urlpatterns = [
    path('', views.index, name='index'),
    path('help/', views.help, name='help'),
    path('register/', views.register, name='register'),
]