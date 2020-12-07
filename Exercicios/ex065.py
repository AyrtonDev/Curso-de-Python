cont = 0
soma = 0
maior = 0
menor = 0
finalizar = False
while not finalizar:
    n = int(input('Digite um número: '))
    cont += 1
    if cont == 1:
        menor = maior = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
    soma += n
    res = str(input('Quer continuar? [S/N] ')).upper()
    if res == 'N':
        finalizar = True
print('Você digitou {} números e a média foi {:.2f}'.format(cont, (soma / cont)))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))