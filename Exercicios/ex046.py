from time import sleep
from emoji import emojize
print('-='*20)
print('Contagem Regressiva para os Fogos de Artificio')
print('-='*20)
sleep(0.5)
for c in range(10, 0, -1):
    print(c)
    sleep(1)
print(emojize('PARABÉNS :fireworks: :fireworks:', use_aliases=True))