from django.urls import path
from bashmycode import views
from django.conf import settings 
from django.conf.urls.static import static

app_name = 'bashmycode'

urlpatterns = [
    path('', views.index, name='index'),
    path('help/', views.help, name='help'),
    path('register/', views.register, name='register'),
    path('profile/<username>/', views.ProfileView.as_view(), name='profile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)