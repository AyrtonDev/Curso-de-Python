while True:
    res = ''
    tuplaNum = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorse', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
    num = 0
    while True:
        num = int(input('Digite um número entre 0 e 20: '))
        if num < 0 or num > 20:
            print('Digite novamente. ', end='')
        else:
            break
    print(f'Você digitou o número {tuplaNum[num]}')
    print('')
    res = str(input('Você quer continuar? [S/N] ')).upper().strip()[0]
    if res == 'N':
        break