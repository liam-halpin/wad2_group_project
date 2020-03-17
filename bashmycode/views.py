from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from .models import Post

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
            return redirect('index')
    else:
        form = UserRegisterForm()
    return render(request, 'bashmycode/register.html', {'form': form})

def bash(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'bashmycode/bash.html', context)

def help(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'bashmycode/help.html', context)