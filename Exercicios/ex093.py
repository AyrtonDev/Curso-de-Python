jogador = dict()

jogador['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
jogador['gols'] = list()
for c in range(0, partidas):
    jogador["gols"].append(int(input(f'Quantos gols na partida {c}? ')))
print('-='*30)
print(jogador)
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
p = 0
jogador['total'] = 0
for c in jogador["gols"]:
    print(f'   => Na partida {p}, fez {c} gols.')
    jogador["total"] += c
    p += 1
print(f'Foi um total de {jogador["total"]} gols.')

# solução do Professor
'''jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome do Jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
 for c in range(0, tot):
    partidas.append(int(input(f'   Quantos gols na partida {c}? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partdas)
print('-='*30)
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'   => Na partida {i}, fez {v} gols')
print(f'Foi um total de {jogador["total"]} gols')'''