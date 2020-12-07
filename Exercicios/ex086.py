matriz = list()
linha = list()
for c in range(0, 3):
    for l in range(0, 3):
        linha.append(int(input(f'Digite um valor para [{c}, {l}]: ')))
    matriz.append(linha[:])
    linha.clear()
print('-='*30)
for m in matriz:
    print(f'[{m[0]:^5}][{m[1]:^5}][{m[2]:^5}]')

# solução Professor
'''matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]:'))
print('-='*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()'''