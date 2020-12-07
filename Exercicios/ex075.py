num = (int(input('Digite o 1º valor: ')),
       int(input('Digite o 2º valor: ')),
       int(input('Digite o 3º valor: ')),
       int(input('Digite o 4º valor: ')))

print(f'Os valores digitados foram: {num}')
if 9 in num:
    print(f'O número 9 apareceu {num.count(9)} vezes.')
else:
    print('O 9 não apareceu nenhuma vez')
if 3 in num:
    print(f'O número 3 aparece na {num.index(3)+1}º posição')
else:
    print('O número 3 não aparece em nenhuma posição!')
print('Os valores pares digitados foram: ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')