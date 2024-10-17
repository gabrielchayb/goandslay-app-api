from core.models import User
from django.shortcuts import render
from core.models import User
from .forms import UserRegistrationForm , UserLoginForm , UserEditForm , LicaoForm
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout 
from django.http import HttpResponseRedirect
from core.models import Licao
from django.shortcuts import get_object_or_404

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
    return HttpResponseRedirect('/user_login') #até aqui OK, tudo funcionando

@login_required
def visualizarperfil(request):
    user = request.user
    return render(request, 'visualizarperfil.html', {'user': user}) 

@login_required
def editarperfil(request):
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Seu perfil foi atualizado com sucesso!')
            return redirect('visualizarperfil')  # Redireciona para o perfil do usuário
    else:
        form = UserEditForm(instance=request.user)
    
    return render(request, 'editarperfil.html', {'form': form})

@login_required
def deletarperfil(request):
    user = request.user
    user.delete()
    messages.success(request, 'Sua conta foi deletada com sucesso.')
    return redirect('index')

@login_required
def cadastrarlicao(request):
    if request.method == 'POST':
        form = LicaoForm(request.POST)
        if form.is_valid():
            licao = form.save(commit=False)
            licao.user = request.user  # Define o usuário logado como autor da lição
            licao.save()
            messages.success(request, 'Lição cadastrada com sucesso!')
            return redirect('home')  # Redireciona para a home
    else:
        form = LicaoForm()
    
    return render(request, 'cadastrarlicao.html', {'form': form})

@login_required
def listar_todas_licoes(request):
    licoes = Licao.objects.all()  # Busca todas as lições no banco de dados
    return render(request, 'visualizarlicao.html', {'licoes': licoes})

@login_required
def editar_licao(request, licao_id):
    licao = get_object_or_404(Licao, id=licao_id, user=request.user)  # Verifica se a lição pertence ao usuário

    if request.method == 'POST':
        form = LicaoForm(request.POST, instance=licao)
        if form.is_valid():
            form.save()
            messages.success(request, 'Lição atualizada com sucesso!')
            return redirect('listar_todas_licoes')  # Redireciona para a lista de todas as lições após a edição
    else:
        form = LicaoForm(instance=licao)

    return render(request, 'editarlicao.html', {'form': form, 'licao': licao})


@login_required
def deletar_licao(request, licao_id):
    licao = get_object_or_404(Licao, id=licao_id, user=request.user)  # Verifica se a lição pertence ao usuário

    if request.method == 'POST':
        licao.delete()
        messages.success(request, 'Lição deletada com sucesso!')
        return redirect('home')  # Redireciona diretamente para a página "home"

    # Redireciona de volta para "home" se a requisição não for POST
    return redirect('home')

