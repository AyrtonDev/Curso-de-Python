cores = {
    'vermelho' : '\033[1;31m',
    'azul' : '\033[4;34m',
    'verde' : '\033[4;32m',
    'limpa' : '\033[m'
}

print('='*10, 'Lojas Muller Danada', '='*10)
preço = float(input('Preço das compras: R$'))
print('FORMAS DE PAGAMENTO')
print('[ 1 ] à vista dinheiro/cheque')
print('[ 2 ] à vista cartão')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x ou mais no cartão')
opção = int(input('Qual é a opção? '))
if opção == 1:
    desc = preço - (preço * 10 / 100)
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, desc))
elif opção == 2:
    desc = preço - (preço * 5 / 100)
    print('Sua compre de R${:.2f} vai custar R${:.2f} no final.'.format(preço, desc))
elif opção == 3:
    parc = preço / 2
    print('Sua compra de R${:.2f} vai ficar 2x de R${:.2f} no final.'.format(preço, parc))
elif opção == 4:
    parc = int(input('Quantas parcelas? '))
    if parc < 3:
        print('Parcelamento INVALIDO! Considerando parcelamente de 3x')
        parc = 3
    novoP = preço + (preço * 20 / 100)
    parcFinal = novoP / parc
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(parc, parcFinal))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, novoP))
else:
    print('Opção INVALIDA!')