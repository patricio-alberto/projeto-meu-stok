from django.contrib.auth.models import User
from django.db import models


class CadastroProduto(models.Model):
    Emb_choices = (
        ('cx', 'Caixa'),
        ('kg', 'Quilograma'),
        ('mt', 'Metro'),
        ('un', 'Unidade')
    )
    descricao = models.CharField(max_length=20)
    tipoEmb = models.CharField(max_length=2, choices=Emb_choices)
    codEmb = models.CharField(max_length=14)


class CadastroEmpresa(models.Model):
    razaosocial = models.CharField(max_length=15)
    cnpj = models.CharField(max_length=15)
    endereco = models.CharField(max_length=30)
    cep = models.CharField(max_length=7)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
