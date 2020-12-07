cores = {
    'limpa' : '\033[m',
    'vermelho' : '\033[31m',
    'verde' : '\033[32m'
}
from random import randint
print('='*20)
print('Vou pensar em um número de {}0 a 10{}. Tente adivinhar...'.format(cores['verde'], cores['limpa']))
print('='*20)
computador = randint(0, 10)
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Em que número pensei? '))
    if jogador != computador:
        if jogador > computador:
            print('{}Menos..{}! Tente Novamente!'.format(cores['vermelho'], cores['limpa']))
        else:
            print('{}Mais...{}! Tente Novamente!'.format(cores['vermelho'], cores['limpa']))
        palpite += 1
        print('')
    else:
        print('{}PARABÉNS{}! Você descobriu!'.format(cores['verde'], cores['limpa']))
        print('')
        acertou = True
print('Você deu {}{}{} palpites para vencer.'.format(cores['vermelho'], palpite, cores['limpa']))