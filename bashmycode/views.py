from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from .models import Post
from django.contrib.auth.decorators import login_required

def index(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'bashmycode/index.html', context)
 

def help(request):
    return render(request, 'bashmycode/help.html', {'title': 'Help'})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('/bashmycode/login')
    else:
        form = UserRegisterForm()
    return render(request, 'bashmycode/register.html', {'form': form})

def bash(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'bashmycode/bash.html', context)

@login_required
def profile(request):
    return render(request, 'bashmycode/profile.html')

# def user_login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(username=username, password=password)

#         if user:
#             if user.is_active:
#                 login(request, user)
#                 return redirect(reverse('bashmycode:index'))
#             else:
#                 return HttpResponse("Your BashMyCode account is disabled.")
#         else:
#             print(f"Invalid login details: {username}, {password}")
#             return HttpResponse("Invalid login details supplied.")
#     else:
#         return render(request, 'bashmycode/login.html')

# @login_required
# def restricted(request):
#     return HttpResponse("You are logged in")

# @login_required
# def user_logout(request):
#     logout(request)
#     return redirect(reverse('bashmycode:index'))
# def help(request):
#     context = {
#         'posts': Post.objects.all()
#     }
#     return render(request, 'bashmycode/help.html', context)
