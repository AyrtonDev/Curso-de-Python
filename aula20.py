# Aulas sobre Def (funções)
def lin():
    print('-' * 30)


lin()
print(f'{"CURSO EM VÍDEO":^30}')
lin()
print(f'{"APRENDA PYTHON":^30}')
lin()
print(f'{"GUSTAVO GUANABARA":^30}')
lin()

def mensagem(msg):
    print('-' * 30)
    print(f'{msg:^30}')
    print('-' * 30)


mensagem('SISTEMA DE ALUNOS')

# def com funções aritmeticas

def soma(a, b):
    c = a + b
    print(c)

soma(5, 4)
soma(8, 9)
soma(2, 1)

# def com tuplas

def contador(* num):
    for valor in num:
        print(f'{valor} ', end='')
    print('FIM!')
    
contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

def soma1(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {num} temos {s}')

soma1(5, 2)
soma1(2, 9, 4)

# def no uso com listas

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)