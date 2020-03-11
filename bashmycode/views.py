from django.shortcuts import render, redirect
from django.http import HttpResponse
from bashmycode.forms import UserForm, UserProfileForm
from django.contrib.auth.models import User
from bashmycode.models import UserProfile
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse

def index(request):
    return render(request, 'bashmycode/index.html')

def help(request):
    return render(request, 'bashmycode/help.html')

def register(request):
    registered = False
    
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            # Save the user to the database using the form data
            user = user_form.save()

            # Hash the password w/ set_password, then update user object
            user.set_password(user.password)
            user.save()

            # Now sort the UserProfile instance
            profile = profile_form.save(commit=False)
            profile.user = user

            # If the user provided a profile image get it from input
            # form and put it in model
            if 'picture' in request.FILES:
                profile_picture = request.FILES['picture']
            
            # Save the UserProfile model instance
            profile.save()

            registered = True    # Registration successfull
        else:
            print(user_form.errors, profile_form.errors)
    else:
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
