print('='*20)
print('Aplicador de Desconto')
print('='*20)
preco = float(input('Digite o valor do produto? '))
novo = preco - (preco * 5 / 100)
print('Aplicando o cupom de 5% desconto fica: {:.2f} R$'.format(novo))