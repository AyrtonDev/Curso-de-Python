print('='*20)
print('CALCULADOR DE TINTA')
print('='*20)
alt = int(input('Qual a altura da parede? '))
larg = int(input('Qual a largura da parede? '))

area = alt * larg
tint = area / 2
print('Uma parade de {}m² precisa de {} Litros de tinta para pinta-la'.format(area, tint))