def area(a, b):
    c = a * b
    print('-' * 30)
    print(f'A área do terreno {a}x{b} é de {c:.1f}m²')
    print('-' * 30)


print()
print('Controle de Terrenos')
print('-' * 30)
larg = float(input('LARGURA (m): '))
comp = float(input('COMPRIMENTO (m): '))
area(larg, comp)