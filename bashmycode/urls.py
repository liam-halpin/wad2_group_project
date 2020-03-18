from django.urls import path, reverse
from bashmycode import views
from django.contrib.auth import views as auth_views
from django.shortcuts import redirect
from django.conf import settings
from django.conf.urls.static import static

app_name = 'bashmycode'

urlpatterns = [
    path('', views.index, name='index'),
    path('help/', views.help, name='help'),
    path('register/', views.register, name='register'),

    path('login/', auth_views.LoginView.as_view(template_name='bashmycode/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='bashmycode/logout.html'), name='logout'),

    path('profile/', views.profile, name='profile'),

    path('bash/', views.bash, name='bash'),
    path('help/', views.help, name='help')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
