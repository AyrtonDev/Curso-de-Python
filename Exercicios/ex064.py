cont = 0
soma = 0
finalizar = False
while not finalizar:
    n = int(input('Digite um número [999 para parar]: '))
    if n != 999:
        cont += 1
        soma += n
    else:
        finalizar = True
print('Você digitou {} números e a soma entre eles foi de {}.'.format(cont, soma))