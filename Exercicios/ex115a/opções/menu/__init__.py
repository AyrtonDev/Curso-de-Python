c = (
    '\033[m',     # limpa
    '\033[0;31m', # vermelho
    '\033[0;33m', # amarelo
    '\033[0;34m'  # azul
)

def painel():
    print(f'{"MENU PRINCIPAL":^40}')
    print('-' * 40)
    print(f'{c[2]}1{c[0]} - {c[3]}Ver pessoas cadastradas{c[0]}')
    print(f'{c[2]}2{c[0]} - {c[3]}Cadastrar nova Pessoa{c[0]}')
    print(f'{c[2]}3{c[0]} - {c[3]}Sair do Sistema{c[0]}')
    print('-' * 40)

def principal():
    while True:
        try:
            painel()
            escolha = int(input(f'{c[2]}Sua Opção:{c[0]} '))
        except (TypeError, ValueError):
            print(f'{c[1]}Erro: por favor, digite um número inteiro válido.{c[0]}')
            print('-' * 40)
            continue
        else:
            return escolha