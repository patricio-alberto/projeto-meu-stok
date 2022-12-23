from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.shortcuts import render # Já tinha
from .forms import Login # Já tinha
from django.contrib.auth.models import User
from .models import CadastroEmpresa as cadempresa


def core(request):
    if request.method == "GET":
        return render(request, 'index.html')
    else:
        username = request.POST.get('usuario')
        senha = request.POST.get('senha')

        user = authenticate(username=username, password=senha)

        if user:
            login(request, user)
            return HttpResponse('Autenticado!')
        else:
            return HttpResponse('Usuário ou senha inválido!')


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
            return HttpResponse('Já existe um usuário cadastrado com esse nome.')
        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()
        return HttpResponse('Usuário cadastrado com sucesso!')


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

        empresa = cadempresa.objects.create(razaosocial=rs, cnpj=cnpj, endereco=endereco, cep=cep)
        empresa.save()
        return HttpResponse('Empresa cadastrada com sucesso!')


# def get_name(request):
#     if request.method == 'POST':
#         form = Login(request.POST)
#         if form.is_valid():
#             return HttpResponseRedirect('tela-usuario')
# Create your views here.

class CampoLogin(CreateView):
    model = Login
    fields = ['usuario', 'senha']
    template_name = 'index.html'
    success_url = reverse_lazy('templates/')

#class CampoCadastro(CreateView):
