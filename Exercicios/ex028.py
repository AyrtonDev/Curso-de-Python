from random import randint
from time import sleep
print('-=-'*15)
print('Vou pensar em um número entre 0 a 5. Tente adivinhar...')
print('-=-'*15)
num = int(input('Em que número pensei? '))
comp = randint(0,5)
print('PROCESSANDO...')
sleep(2)
if num == comp:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}'.format(comp, num))