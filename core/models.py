from django.db import models

class Login(models.Model):
    usuario = models.EmailField(max_length=80)
    senha = models.CharField(max_length=20)

    def __str__(self):
        pass

class Cadastro(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=80)
    senha = models.CharField(max_length=60)
    confSenha = models.CharField(max_length=60)


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