# aula sobre Variáveis compostas (Tuplas)

'''lanche = ('Hambúguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
print(lanche[-3:])
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

print('Comi pra caramba!')

print(sorted(lanche))
print(lanche)'''

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
print(len(c))
print(c.count(c))
print(c.index(5, 1))

pessoa = ('Ayrton', 25, 'M', 157.60)