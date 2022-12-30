from django.urls import path
from .views import *


urlpatterns = [
    path('', core, name='inicio'),
    path('sair/', sair, name='sair'),
    path('templates/', TelaUsuario, name='templates'),
    path('cadastro/', Cadastro, name='cadastro'),
    path('cadastro-produto/', CadastroProduto, name='cadastroproduto'),
    path('cadastro-empresa/', CadastroEmpresa, name='cadastroempresa'),
    path('listar_empresas/', ListarEmpresa, name='listarempresa')
]
