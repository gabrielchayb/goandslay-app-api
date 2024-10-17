from core.models import User
from django.shortcuts import render
from core.models import User
from .forms import UserRegistrationForm , UserLoginForm
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout 
from django.http import HttpResponseRedirect

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro bem-sucedido! Você pode agora fazer login.')
            return redirect('user_login')  # Altere 'login' para o nome da URL de login
    else:
        form = UserRegistrationForm()
    
    return render(request, 'register.html', {'form': form})

def user_login(request):  # Renomeie a função para evitar conflito
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            # Tenta autenticar o usuário
            user = authenticate(request, email=email, password=password)
            
            if user is not None:
                auth_login(request, user)  # Usa a função de login correta
                return redirect('home')  # Redireciona para a página inicial
            else:
                messages.error(request, "Credenciais inválidas. Tente novamente.")
    
    else:
        form = UserLoginForm()  # Cria uma nova instância do formulário
    
    return render(request, 'user_login.html', {'form': form})


@login_required  # Garantir que o usuário esteja autenticado
def home(request):
    user = request.user  # Obtém o usuário logado
    return render(request, 'home.html', {'user': user})  # Passa o usuário para o template

@login_required
def sair(request):
    logout(request)
    return HttpResponseRedirect('/user_login')
