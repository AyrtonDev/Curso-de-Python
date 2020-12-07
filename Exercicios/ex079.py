valores = []
while True:
    res = ''
    num = int(input('Digite um valor: '))
    if num in valores:
        print('Valor duplicado! Não vou adicionar...')
    else:
        valores.append(num)
        print('Valor adicionado com sucesso...')
    res = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if res == 'N':
        break
    print('-'*30)
print('='*30)
valores.sort()
print(f'Você digitou os valores {valores}')