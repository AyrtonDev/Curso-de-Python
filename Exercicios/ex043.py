cores = {
    'amarelo' : '\033[4;33m',
    'azul' : '\033[34m',
    'verde' : '\033[32m',
    'vermelho' : '\033[1;31m',
    'limpa' : '\033[m'
}

print('Calculadora de IMC')
print('-'*20)
peso = float(input('Qual é seu peso? (Kg)'))
altura = float(input('Qual é a sua altura? (m)'))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está {}ABAIXO DO PESO{} normal'.format(cores['amarelo'], cores['limpa']))
elif imc < 25:
    print('PARABÉNS, você está na faixa de {}PESO NORMAL{}'.format(cores['verde'], cores['limpa']))
elif imc < 30:
    print('Você está em {}SOBREPESO{}'.format(cores['azul'], cores['limpa']))
elif imc < 40:
    print('Você está em {}OBESIDADE{}'.format(cores['amarelo'], cores['limpa']))
else:
    print('Você está em {}OBESIDADE MÓRBIDA{}, cuidado!'.format(cores['vermelho'], cores['limpa']))