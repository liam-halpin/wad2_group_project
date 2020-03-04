from django.shortcuts import render
from django.http import HttpResponse
from bashmycode.forms import UserForm, UserProfileForm

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