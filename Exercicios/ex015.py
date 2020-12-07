dia = int(input('Quantos dias o carro foi alugado? '))
km = int(input('Quantos Quilometros o carro rodou? '))
preço = (dia * 60) + (km * 0.15)
print('O total a pagar é de R${:.2f}'.format(preço))