from random import randint
maior = menor = 0
numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1 ,10))
for cont in range(0, len(numeros)):
    if cont == 0:
        maior = menor = numeros[cont]
    else:
        if numeros[cont] > maior:
            maior = numeros[cont]
        if numeros[cont] < menor:
            menor = numeros[cont]
print(f'Os valores sorteados foram: {numeros}')
print(f'O maior valor sorteado foi {maior}')
print(f'O menor valor sorteado foi {menor}')