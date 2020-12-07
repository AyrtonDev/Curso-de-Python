print('-'*30)
valores= []
while True:
    res = ''
    num = int(input('Digite um número: '))
    if num in valores:
        print('Número duplicado! Não sera adicionado a lista...')
    else:
        valores.append(num)
        print('Valor adicionado a lista...')
    res = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if res == 'N':
        break
    print('-'*30)
print('*'*30)
print(f'Foram digitados {len(valores)} números')
valores.sort(reverse = True)
print(f'Os valores em ordem decrescente são {valores}')
if 5 in valores:
    print('O valor 5 está na lista')
else:
    print('O valor 5 não está na lista')