tot = []
impar = []
par = []
while True:
    res = ''
    num = int(input('Digite um número: '))
    if num in tot:
        print('Número dupliacado! Digite outro valor...')
    else:
        tot.append(num)
        if num % 2 == 0:
            par.append(num)
        else:
            impar.append(num)
    res = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if res == 'N':
        break
print('-='*30)
print(f'A lista completa é {tot}')
print(f'A lis de pares é {par}')
print(f'A lista de ímpares é {impar}')