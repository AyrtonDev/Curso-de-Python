cores = {
    'lilas' : '\033[4;35m',
    'vermelho' : '\033[1;31m',
    'limpa' : '\033[m'
}

print('-='*15)
n1 = int(input('Primeiro numero: '))
n2 = int(input('Segundo numero: '))

if n1 == 0 or n2 == 0:
    print('{}[ERRO]{} Digite um numero valido!'.format(cores['vermelho'], cores['limpa']))
else:
    if n1 > n2:
        print('O {}PRIMEIRO{} valor e maior'.format(cores['lilas'], cores['limpa']))
    elif n2 > n1:
        print('O {}SEGUNDO{} valor e maior'.format(cores['lilas'], cores['limpa']))
    else:
        print('Os dois valores sao {}IGUAIS{}'.format(cores['lilas'], cores['limpa']))