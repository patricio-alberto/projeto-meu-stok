from django.urls import path
from django.views.generic import TemplateView 
from .views import *


urlpatterns = [
    path('', core),
    path('templates/', TelaUsuario, name='templates'),
    path('cadastro/', Cadastro, name='cadastro'),
    path('cadastro-produto/', CadastroProduto, name='cadastroproduto'),
    path('cadastro-empresa/', CadastroEmpresa, name='cadastroempresa')
]
