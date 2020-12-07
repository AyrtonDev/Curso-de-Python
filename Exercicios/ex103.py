def ficha(nome, gols):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


print('-' * 30)
nome = str(input('Nome do Jogador: '))
gol = str(input('Número de Gols: '))
if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0
if nome == '':
    nome = '<desconhecido>'
ficha(nome, gol)

# solução do professor
'''def ficha(jog='<desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')


n = str(input('Nome do Jogador: '))
g = str(input('Número de Gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if b.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)'''