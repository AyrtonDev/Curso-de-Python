num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
print('=='*15)
c = 0
while c != 5:
    print('''
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa
    ''')
    c = int(input('Qual a sua opção? '))
    if c == 1:
        print('A soma dos valores {} e {} é {}'.format(num1, num2, (num1 + num2)))
    elif c == 2:
        print('A multiplicação dos valores {} e {} é {}'.format(num1, num2, (num1 * num2)))
    elif c == 3:
        if num1 > num2:
            print('O maior número é {}'.format(num1))
        else:
            print('O maior número é {}'.format(num2))
    elif c == 4:
        num1 = int(input('Digite o primeiro valor: '))
        num2 = int(input('Digite o segundo valor: '))
    elif c == 0 or c > 5:
        print('Opção inválida! Por favor escolha novamente!')
    print('-'*20)
print('Fim do programa')       