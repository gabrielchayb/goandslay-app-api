from core.models import User
from django.shortcuts import render
from core.models import User
from .forms import UserRegistrationForm
from django.shortcuts import redirect
from django.contrib import messages

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro bem-sucedido! Você pode agora fazer login.')
            return redirect('login')  # Altere 'login' para o nome da URL de login
    else:
        form = UserRegistrationForm()
    
    return render(request, 'register.html', {'form': form})