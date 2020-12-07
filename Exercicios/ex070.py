print('-'*20)
print('   LOJA SUPER DB   ')
print('-'*20)
nomeP = ''
custop = produtosE = totGasto = 0
while True:
    preço = 0
    continuar = ''
    produto = str(input('Nome do produto: '))
    while True:
        preço = int(input('Preço: R$'))
        if preço > 0:
            break
    if preço < 1000:
        produtosE += 1
    if custop == 0 or preço < custop:
        custop = preço
        nomeP = produto
    totGasto += preço
    while True:
        continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if continuar in 'SN':
            break
    print('-'*20)
    if continuar == 'N':
        break
print('- '*6, 'FIM DO PROGRAMA', ' -'*6)
print(f'O total da compra foi R${totGasto:.2f}')
print(f'Temos {produtosE} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nomeP} que custa R${custop:.2f}')