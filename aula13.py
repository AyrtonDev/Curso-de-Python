# Aula introdutoria aos laços de repetição FOR

'''for c in range(1, 10):
    print(c)
print('FIM')'''

i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('FIM')