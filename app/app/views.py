# app/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Loga o usuário após o registro
            return redirect('home')  # Redireciona para a página home
    else:
        form = UserCreationForm()
    
    return render(request, 'register.html', {'form': form})

def login(request):
    return render(request, 'login.html')

@login_required
def home(request):
    user = request.user
    return render(request, 'home.html', {'user': user})

@login_required
def user_info(request):
    user = request.user
    return render(request, 'user_info.html', {'user': user})