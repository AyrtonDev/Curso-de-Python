menorPeso = 0
maiorPeso = 0
for pess in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(pess)))
    if pess == 1:
        maiorPeso = peso
        menorPeso = peso
    else:
        if peso > maiorPeso:
            maiorPeso = peso
        if peso < menorPeso:
            menorPeso = peso
print('')
print('O maior peso lido foi de {:.1f}Kg'.format(maiorPeso))
print('O menor peso lido foi de {:.1f}Kg'.format(menorPeso))