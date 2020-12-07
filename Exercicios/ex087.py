matriz = list()
linha = list()
somaPares = 0
maior2l = 0
for c in range(0, 3):
    for l in range(0, 3):
        num = (int(input(f'DIgite um valor para [{c}, {l}]: ')))
        linha.append(num)
        if num % 2 == 0:
            somaPares += num
    matriz.append(linha[:])
    linha.clear()
print('-='*30)
for m in matriz:
    print(f'[{m[0]:^5}][{m[1]:^5}][{m[2]:^5}]')
print('-='*30)
soma3c = matriz[0][2] + matriz[1][2] + matriz[2][2]
for l in matriz[1]:
    if maior2l == 0:
        maior2l = l
    else:
        if maior2l < l:
            maior2l = l
print(f'A soma dos valores pares é {somaPares}')
print(f'A soma dos valores da terceira coluna é {soma3c}')
print(f'O maior valor da segunda linha é {maior2l}')
