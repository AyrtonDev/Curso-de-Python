coleção = list()
numeros = list()
for c in range(1, 8):
    num = int(input(f'Digite o {c}º valor: '))
    if num % 2 == 0:
        numeros.append('par')
        numeros.append(num)
    else:
        numeros.append('impar')
        numeros.append(num)
    coleção.append(numeros[:])
    numeros.clear()
print('-='*30)
coleção.sort()
print('Os valores pares digitados foram: ', end='')
for c in coleção:
    if 'par' in c[0]:
        print(f'{c[1]}', end=' ')
print()
print('Os valores ímpares digitados foram: ', end='')
for c in coleção:
    if 'impar' in c[0]:
        print(f'{c[1]}', end=' ')

# solução do professor
'''num = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print('-='*30)
num[0].sort()
num[1].sort()
print(f'Os valores pares digitados foram: {num[0]}')
print(f'Os valores ímpares digitados foram: {num[1]}')'''