# Colocação do campeonato Brasilerão de 2020. Dados retirados na data 20 de novembro de 2020
colocação = ('Atlético-MG', 'Internacional', 'São Paulo', 'Flamengo', 'Palmeiras', 'Santos', 'Grêmio', 'Fluminense', 'Bahia', 'Athletico-PR', 'Sport Recife', 'Fortaleza', 'Corinthians', 'Ceará SC', 'Atlético-GO', 'Vasco da Gama', 'Bragantino', 'Coritiba', 'Botafogo', 'Goiás')
print('-='*15)
print(f'Lista de times do Brasileirão: {colocação}')
print('-='*15)
print(f'Os 5 primeiros são {colocação[0:5]}')
print('-='*15)
print(f'Os 4 últimos são {colocação[-4:]}')
print('-='*15)
print(f'Times em ordem alfabética: {sorted(colocação)}')
print('-='*15)
print(f'O {colocação[7]} está na {colocação.index("Fluminense")+1}ª posição')