cores = {
    'limpa' : '\033[m',
    'azul' : '\033[1;34m',
    'lilas' : '\033[4;35m',
    'vermelho' : '\033[1;31m'
}
print('-='*15)
print('|  Analisador de Triângulos  |')
print('-='*15)
r1 = int(input('Primeiro segmento: '))
r2 = int(input('Segundo segmento: '))
r3 = int(input('Terceiro segmento: '))
print('-='*10)
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima {}PODEM FORMAR{} um triângulo!'.format(cores['azul'], cores['limpa']))
    if r1 == r2 == r3:
        print('Triângulo {}EQUILÁTERO{}!'.format(cores['lilas'], cores['limpa']))
    elif r1 != r2 != r3 != r1:
        print('Triângulo {}ESCALENO{}!'.format(cores['lilas'], cores['limpa']))
    else:
        print('Triângulo {}ISÓSCELES{}!'.format(cores['lilas'], cores['limpa']))
else:
    print('Os segmentos acima {}NÃO PODEM FORMAR{} um triângulo!'.format(cores['vermelho'], cores['limpa']))