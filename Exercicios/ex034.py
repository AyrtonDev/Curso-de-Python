salario = float(input('Digite o salário do funcionário: '))
if salario > 1250:
    novo = salario + (salario * 10 / 100)
    print('Com aumento de 10% o novo salário será de {:.2f} reais.'.format(novo))
else:
    novo = salario + (salario * 15 / 100)
    print('Com o aumento de 15% o novo salário será de {:.2f} reais.'.format(novo))