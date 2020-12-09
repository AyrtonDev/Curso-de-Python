from opções import cadastrar, lista, menu
from time import sleep

while True:
    escolha = menu.principal()
    if escolha == 1:
        print()
    elif escolha == 2:
        print()
    elif escolha == 3:
        break
    else:
        print('\033[0;31mOpção inválida! Escolha Novamente.\033[m')
        print('-' * 40)
    sleep(1)
print('-' * 40)
print(f'{"Saindo do sistema... Até logo!":^40}')
print('-' * 40)