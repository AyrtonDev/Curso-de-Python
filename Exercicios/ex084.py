pessoas = list()
dados = list()
pesoMax = list()
pesoMin = list()
menorP = 0
while True:
    res = ''
    dados.append(str(input('Digite seu nome: ')))
    dados.append(float(input('Digite seu peso em Kg: ')))
    if menorP == 0:
        menorP = dados[1]
    else:
        if menorP > dados[1]:
            menorP = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    res = str(input('Quer continuar? ')).upper().strip()[0]
    if res == 'N':
        break
    print('-'*30)
print('='*30)
for p in pessoas:
    if p[1] >= 100:
        pesoMax.append(p[0])
    else:
        pesoMin.append(p[0])
print(f'Foram cadastrados no total {len(pessoas)} pessoas.')
print(f'Essas foram as pessoas mais pesadas: ', end='')
for c in pesoMax:
    print(f'{c}', end='  ')
print()
print(f'Essas foram as pessoas mais leves: ', end='')
for c in pesoMin:
    print(f'{c}', end='  ')
print()
print(f'O menor peso foi de {menorP:.2f}Kg.')