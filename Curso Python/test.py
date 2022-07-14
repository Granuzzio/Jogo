# Test de conhecimento
from time import sleep

nome = input('Ola Qual o seu nome? ')
idade = input(f'Ola {nome}, prazer em conhecer, Qual a sua idade? ')
idade = int(idade)
idade_minima = 18

if idade >= idade_minima:
    print('ok, vamos prosseguir com seu cadastro')
else:
    print('Nao podemos dar continuidade em seu cadastro porque e menor de idade')
    sleep(2.0)


email = input('Qual seu email? ')
nome_mae = input('Qual o nome da sua mae? ')
nome_pai = input('Qual o nome do seu pai? ')
confirmacao = input(f'O nome da sua mae e {nome_mae} e o nome do seu pai e {nome_pai}. Vamos Continuar. ')
usuario = input('Digite o nome para seu login: ')
senha = input('Digite uma senha: ')
print('Cadastro realizado com sucesso, Voce ja pode logar em sua conta')

usuario_bd = input('Qual o seu nome de usuario? ')
senha_bd = input('Qual a sua senha? ')

if usuario == usuario_bd and senha == senha_bd:
    print('Voce esta logado')
else:
    print('Usuario ou a senha estao incorretos, tente novamente !!!')
