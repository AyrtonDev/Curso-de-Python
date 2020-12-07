from random import randint
from time import sleep

def sorteio():
    valores = [randint(1, 10), randint(1, 10), 
    randint(1, 10), randint(1, 10), randint(1, 10)]
    print('Sorteando 5 valores da lista:', end=' ')
    for c in valores:
        sleep(0.5)
        print(f'{c}', end=' ')
    print('PRONTO!')
    return valores

def somaPar(lst):
    tot = 0
    for c in lst:
        if c % 2 == 0:
            tot += c
    print(f'Somando os valores pares de {lst}, temos {tot}')

somaPar(sorteio())

# Solução do Professor

'''def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='', flush=True)
        sleep(0.3)
    print('PRONTO!')


def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma+= valor
    print(f'Somando os valores pares de {lista}, temos {soma}')


numeros = list()
sorteia(numeros)
somaPar(numeros)'''