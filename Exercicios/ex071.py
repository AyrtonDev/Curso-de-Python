print('='*30)
print('{:^30}'.format('BANCO DA AMAZONIA'))
print('='*30)
valor = int(input('Qual valor a ser sacado? R$'))
total = valor
ced = 50
totCed = 0
while True:
    if ced <= total:
        total -= ced
        totCed += 1
    else:
        if totCed > 0:
            print(f'Total de {totCed} cédulas de R${ced:.2f}')
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 1
        totCed = 0
        if total == 0:
            break
print('='*30)
print('Volte sempre ao BANCO DA AMAZONIA! Tenha um otimo dia!')