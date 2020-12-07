from random import randint
from time import sleep
from operator import itemgetter
player = dict()

for c in range(1, 5):
    player[f'jogador{c}'] = randint(1,6)
print('Valores sorteados:')
for k, v in player.items():
    print(f'   O {k} tirou {v}')
    sleep(1)
print('Ranking dos jogadores:')
ordenado = list()
ordenado = sorted(player.items(), key=itemgetter(1), reverse= True)
for c, l in enumerate(ordenado):
    print(f'{c+1}º lugar: {l[0]} com {l[1]}.')
    sleep(1)

# Solução do professor
'''from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
ranking = list()
print('Valores sorteados:')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-='*30)
print('  == RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f'   {i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)'''