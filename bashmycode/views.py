from django.shortcuts import render, redirect
<<<<<<< HEAD
from django.http import HttpResponse
from bashmycode.forms import UserForm, UserProfileForm
from django.contrib.auth.models import User
from bashmycode.models import UserProfile
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse
=======
from django.contrib import messages
from .forms import UserRegisterForm
>>>>>>> updated register view

def index(request):
    return render(request, 'bashmycode/index.html')

def help(request):
    return render(request, 'bashmycode/help.html', {'title': 'Help'})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('index')
    else:
<<<<<<< HEAD
        user_form = UserForm()
        profile_form = UserProfileForm()
    
    return render(request, 'bashmycode/register.html', context={'user_form': user_form, 'profile_form': profile_form, 'registered': registered})


class ProfileView(View): 
    def get_user_details(self, username): 
        try: 
            user = User.objects.get(username=username) 
        except User.DoesNotExist: 
            return None

        user_profile = UserProfile.objects.get_or_create(user=user)[0] 
        form = UserProfileForm({'website': user_profile.website, 'picture': user_profile.picture})
        return (user, user_profile, form)


    @method_decorator(login_required) 
    def get(self, request, username): 
        try: 
            (user, user_profile, form) = self.get_user_details(username) 
        except TypeError: 
            return redirect(reverse('rango:index'))

        context_dict = {'user_profile': user_profile, 'selected_user': user, 'form': form}
        return render(request, 'bashmycode/profile.html', context_dict)


    @method_decorator(login_required) 
    def post(self, request, username): 
        try: 
            (user, user_profile, form) = self.get_user_details(username) 
        except TypeError: 
            return redirect(reverse('rango:index'))

        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)

        if form.is_valid(): 
            form.save(commit=True) 
            return redirect('rango:profile', user.username) 
        else: 
            print(form.errors)

        context_dict = {'user_profile': user_profile, 'selected_user': user, 'form': form}
        return render(request, 'bashmycode/profile.html', context_dict)
=======
        form = UserRegisterForm()
    return render(request, 'bashmycode/register.html', {'form': form})
>>>>>>> updated register view
