jogador = dict()
rank = list()
while True:
    res = ''
    jogador['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    jogador['gols'] = list()
    for c in range(0, partidas):
        jogador['gols'].append(int(input(f'Quantos gols na partida {c}? ')))
    jogador['total'] = sum(jogador['gols'])
    rank.append(jogador.copy())
    jogador.clear()
    while True:
        res = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if res in 'SN':
            break
        else:
            print('[ERRO] Digite apenas S ou N.')
    if res == 'N':
        break
    print('--'*25)
print('-='*25)
print(f'{"cod":<4}{"nome":<15}{"gols":<15}{"total":<6}')
print('-'*40)
for k, v in enumerate(rank):
    print(f'{k:>3}', end=' ')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*40)
while True:
    res = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if res == 999:
        break
    if res >= len(rank):
        print(f'[ERRO] Não existe jogador com o código {res}!')
        print('-'*40)
    else:
        print(f' -- LEVATAMENTO DO JOGADOR {rank[res]["nome"]}:')
        for c, v in enumerate(rank[res]['gols']):
            print(f'No jogo {c+1} fez {v} gols.')
        print('-'*40)
print('<< VOLTE SEMPRE >>')