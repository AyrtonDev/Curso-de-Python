vel = int(input('Digite a velocidade do carro: '))
if vel > 80:
    multa = (vel - 80) * 7
    print('Você excedeu a velocidade permitida! Sua multa é de R${:.2f}'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')