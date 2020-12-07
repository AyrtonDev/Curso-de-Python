import math

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))

hypo = math.hypot(ca, co)

print('O comprimento da hipotenusa é {:.2f}.'.format(hypo))