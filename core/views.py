from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect  # Já tinha
from .forms import Login # Já tinha
from django.contrib.auth.models import User
from .models import CadastroEmpresa as cadempresa
from django.contrib import messages


def core(request):
    if request.user.is_authenticated:
        return redirect('templates')
    else:
        if request.method == "GET":
            return render(request, 'index.html')
        else:
            username = request.POST.get('usuario')
            senha = request.POST.get('senha')

            user = authenticate(username=username, password=senha)

            if user:
                login(request, user)
                return redirect('templates')
            else:
                messages.success(request, 'Usuário ou senha inválido!')
                return redirect('inicio')


@login_required
def TelaUsuario(request):
        return render(request, 'tela-usuario.html')


def Cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    else:
        username = request.POST.get('usuario')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = User.objects.filter(username=username).first()
        if user:
            messages.success(request, 'Já existe um usuário cadastrado com esse nome.')
            return redirect('cadastro')
        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()
        messages.success(request, 'Usuário cadastrado com sucesso!')
        return redirect('inicio')


@login_required
def CadastroProduto(request):
    return render(request, 'cadastro-produto.html')


@login_required
def CadastroEmpresa(request):
    if request.method == "GET":
        return render(request, 'cadastro-empresa.html')
    else:
        rs = request.POST.get('empresa')
        cnpj = request.POST.get('cnpj')
        endereco = request.POST.get('endereco')
        cep = request.POST.get('cep')
        usu = User.objects.get(id=request.user.id)

        empresa = cadempresa.objects.create(razaosocial=rs, cnpj=cnpj, endereco=endereco, cep=cep, user=usu)
        if empresa:
            empresa.save()
            messages.success(request, 'Empresa cadastrada com sucesso!')
            return redirect('templates')
        else:
            messages.success(request, 'Verifique o processo!')


# def get_name(request):
#     if request.method == 'POST':
#         form = Login(request.POST)
#         if form.is_valid():
#             return HttpResponseRedirect('tela-usuario')
# Create your views here.
@login_required
def ListarEmpresa(request):
    empresa = cadempresa.objects.filter(user=request.user.id)
    return render(request, 'empresas.html', {'empresa': empresa})

@login_required
def sair(request):
    logout(request)
    return redirect('inicio')
