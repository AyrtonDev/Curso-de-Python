def cor(n):
    c = (
    '\033[m',     # limpa
    '\033[0;31m', # vermelho
    '\033[0;33m', # amarelo
    '\033[0;34m'  # azul
    )
    return c[n]


def painel():
    print('-' * 40)
    print(f'{"MENU PRINCIPAL":^40}')
    print('-' * 40)
    print(f'{cor(2)}1{cor(0)} - {cor(3)}Ver pessoas cadastradas{cor(0)}')
    print(f'{cor(2)}2{cor(0)} - {cor(3)}Cadastrar nova Pessoa{cor(0)}')
    print(f'{cor(2)}3{cor(0)} - {cor(3)}Sair do Sistema{cor(0)}')
    print('-' * 40)


def principal():
    while True:
        try:
            painel()
            escolha = int(input(f'{cor(2)}Sua Opção:{cor(0)} '))
        except (TypeError, ValueError):
            print(f'{cor(1)}Erro: por favor, digite um número inteiro válido.{cor(0)}')
            print('-' * 40)
            continue
        else:
            return escolha


def leiaInt(n):
    while True:
        try:
            num = int(input(n))
        except (ValueError, TypeError):
            print(f'{cor(1)}ERRO: por favor, digite um número inteiro válido.{cor(0)}')
            continue
        except KeyboardInterrupt:
            print(f'{cor(1)}Usuário preferiu nãi digitar esse número.{cor(0)}')
            return 0
        else:
            return num