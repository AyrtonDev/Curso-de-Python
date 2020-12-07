# aulas sobre funções parte 2: Interactive help, docstrings, Argumentos opcionais, Escopo de variáveis, Retorno de resultados

'''help(print)

print(input.__doc__)'''
# ^ usadp para decobrir oq os camandos, funçoes e palavras reservadas do python fazem!

'''def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    c = i
    while c < f:
        print(f'{c}', end='.. ')
        c += p
    print('FIM!')'''

# docstring para deixar declarações de def's com help()

'''def somar(a=0, b=0, c=0):
    s = a + b + c
    return s

r1 = somar(b=4, c=2)
r2 = somar(3, 2, 5)
r3 = somar(4)
print(f'Meus cálculos deram {r1}, {r2} e {r3}.')'''

# parametros opcionais com return

def teste():
    x = 8
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')


x = n = 2
print(f'No programa principal, n vale {n}')
teste()
print(f'No programa principal, x vale {x}')

def teste1(b):
    global a
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')


a = 5
teste1(a)
print(f'A fora vale {a}')

# escopo de variaveis