# Aula fala sobre listas (vetores) em python
'''num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse = True)
num.insert(2, 2)
#num.pop()
num.remove(2)
print(num)
print(f'Essa lista tem {len(num)} elementos.')
for c, n in enumerate(num):
    print(f'Na posição {c} encontrei o valor {n}!')
print('Cheguei ao final da lista.')'''

a = [2, 3, 4, 7]
#Copia com ligação entre listas
# b = a
#fazer copia de lista sem ligação
b = a[:]
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')