from django.views.generic.edit import CreateView

from .models import Login

from django.urls import reverse_lazy 

from django.shortcuts import render # Já tinha

from .forms import Login # Já tinha


def core(request):
    return render(request, 'index.html')

def TelaUsuario(request):
    return render(request, 'tela-usuario.html')

def Cadastro(request):
    return render(request, 'cadastro.html')

def CadastroProduto(request):
    return render(request, 'cadastro-produto.html')

def CadastroEmpresa(request):
    return render(request, 'cadastro-empresa.html')

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
