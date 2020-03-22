from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from .models import Post
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'bashmycode/index.html')

# Bug here that displays all posts on bash (DOESN'T)
class PostListViewBash(ListView):
    model = Post
    queryset = Post.objects.filter(post_type='BASH').order_by('-date_posted')
    template_name = 'bashmycode/bash.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 2


class PostListViewHelp(ListView):
    model = Post
    queryset = Post.objects.filter(post_type='HELP').order_by('-date_posted')
    template_name = 'bashmycode/help.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 2

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'post_type']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'post_type']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/bashmycode/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def bash(request):
    context = {
        'posts': Post.objects.filter(post_type='BASH').order_by('-date_posted')
    }
    return render(request, 'bashmycode/bash.html', context)

def help(request):
    context = {
        'posts': Post.objects.filter(post_type='HELP').order_by('-date_posted')
    }
    return render(request, 'bashmycode/bash.html', context)
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

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('/bashmycode/profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'bashmycode/profile.html', context)