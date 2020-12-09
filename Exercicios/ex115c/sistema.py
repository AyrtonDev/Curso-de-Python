from opções.menu import principal, leiaInt
from opções.arquivo import *
from opções.cadastrar import cadastrar
from time import sleep

arq = '/home/ayrton/codigos/Curso em Video/python/Exercicios/ex115c/cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    escolha = principal()
    if escolha == 1:
        lerArquivo(arq)
    elif escolha == 2:
        print('-' * 40)
        print(f'{"NOVO CADASTRO":^40}')
        print('-' * 40)
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif escolha == 3:
        break
    else:
        print('\033[0;31mOpção inválida! Escolha Novamente.\033[m')
        print('-' * 40)
    sleep(1)
print('-' * 40)
print(f'{"Saindo do sistema... Até logo!":^40}')
print('-' * 40)