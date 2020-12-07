from random import randint
from time import sleep
sena = list()
print('-'*30)
print(f'{"JOGA NA MEGA SENA":^30}')
print('-'*30)
num = int(input('Quantos jogos você quer que eu sorteie? '))
print('-='*3, f" SORTEANDO {num} JOGOS ", '-='*3)
for c in range(1, (num+1)):
    while True:
        n = randint(1, 60)
        if len(sena) == 6:
            break
        else:
            if not n in sena:
                sena.append(n)
    print(f'Jogo {c}: {sena}')
    sena.clear()
    sleep(1)
print('-='*5, " BOA SORTE ", '-='*5)
