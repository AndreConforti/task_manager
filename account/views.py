## Regras de importação:

## Primeiramente, módulos do Django. Eles são a base do aplicativo Django
## Logo após, módulos do app e locais
## Por fim, bibliotecas de terceiros
from django.contrib import auth
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from .utils import *


@login_required
def index(request):
    return render(request, 'index.html')


def log_in(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/')    ## Se já está logado, não precisa logar de novo
        return render(request, 'login.html')    
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        ## Apenas confirma se esse usuário já está cadastrado no banco
        current_user = auth.authenticate(request, username=username, password=password)

        if not current_user:
            messages.add_message(request, constants.ERROR, 'Usuário ou Senha inválidos.')
            return redirect('/account/log_in')
        else:
            auth.login(request, current_user)  ## Se está cadastrado, efetua o login e envia para o index
            return redirect('/')  ## Redireciona para a index. Isso evita problemas com o recarregamento da página e outros comportamentos inesperados.
    
        
def register(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/')  ## Se já está logado, não precisa se cadastrar
        return render(request, 'register.html')
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if not validate_password(request, password, confirm_password):
            return redirect('/account/register')

        #TODO: realizar as validações inclusive para verificar o e-mail se é válido
        try:
            user = User.objects.create_user(
                username=username,
                password=password,
                email=email,
                is_active=False
            )
            user.save()

            token = create_token(user, email)

            if send_email(username, email, token):
                messages.add_message(request, constants.SUCCESS, 'Usuário cadastrado com sucesso. Verifique sua caixa de entrada para ativar sua conta.')
            
            return redirect(reverse('account:log_in'))
        except:
            messages.add_message(request, constants.ERROR, 'Não foi possível cadastrar este usuário')
            return redirect(reverse('account:register'))


def log_out(request):
    auth.logout(request)
    messages.add_message(request, constants.WARNING, 'Você acaba de sair do TASK MANAGER')
    return redirect(reverse('account:log_in'))


def activate_account(request, token):
    try:
        token = get_object_or_404(Activation, token=token)  ## Verifica se esse token existe. Caso contrário retorna uma página 404
    except Http404:  ## Caso abra uma página 404, volta para a página de login com uma mensagem de erro
        messages.add_message(request, constants.ERROR, 'O token não está cadastrado.')
        return redirect(reverse('account:log_in'))
    else:  ## Realiza estas ações caso o TRY for bem sucedido
        if token.active:
            messages.add_message(request, constants.WARNING, 'Este token já foi ativado.')
            return redirect(reverse('account:log_in'))
        
        user = User.objects.get(username=token.user.username)
        user.is_active = True
        user.save()

        token.active = True
        token.save()

        messages.add_message(request, constants.SUCCESS, 'Conta ativada com sucesso.')
        return redirect(reverse('account:log_in'))
