# Generated by Django 4.1.3 on 2022-12-04 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_login_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cadastro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=80)),
                ('senha', models.CharField(max_length=60)),
                ('confSenha', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='CadastroEmpresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razaosocial', models.CharField(max_length=15)),
                ('cnpj', models.CharField(max_length=15)),
                ('endereco', models.CharField(max_length=30)),
                ('cep', models.CharField(max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='CadastroProduto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=20)),
                ('tipoEmb', models.CharField(choices=[('cx', 'Caixa'), ('kg', 'Quilograma'), ('mt', 'Metro'), ('un', 'Unidade')], max_length=2)),
                ('codEmb', models.IntegerField(max_length=14)),
            ],
        ),
        migrations.AlterField(
            model_name='login',
            name='usuario',
            field=models.EmailField(max_length=80),
        ),
    ]
