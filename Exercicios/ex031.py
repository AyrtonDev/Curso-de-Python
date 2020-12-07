distancia = float(input('Digite a distância de sua viagem em Km? '))
if distancia > 200:
    preço = distancia * 0.45
    print('Sua viagem custará R${:.2f}'.format(preço))
else:
    preço = distancia * 0.5
    print('Sua viagem custará R${:.2f}'.format(preço))
print('Tenha uma otima viagem!')