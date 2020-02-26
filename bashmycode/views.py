from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'bashmycode/index.html')

def help(request):
    return render(request, 'bashmycode/help.html')
