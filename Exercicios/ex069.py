print('-'*25)
print('ANALISADOR DE DADOS')
print('-'*25)
homens = 0
mulheres = 0
maiores = 0
while True:
    idade = 0
    sexo = ''
    continuar = ''
    while True: 
        idade = int(input('Digite a idade: '))
        if idade < 0:
            print('Idade inválida, digite novamente')
            print('')
        else:
            print('')
            break
    while True:
        sexo = str(input('Digite o sexo: [M/F] ')).upper().strip()
        if sexo in 'FM':
            print('')
            break
        else:
            print('Dado inválido, digite novamente')
            print('')
    if idade >= 18:
        maiores += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres += 1
    while True:
        continuar = str(input('Você quer continuar? [S/N] ')).upper().strip()
        if continuar in 'SN':
            break
    if continuar in 'N':
        break
    print('='*25)
print(f'Teve um total de {maiores} pessoas maiores de 18 anos.')
print(f'Foram {homens} homens cadastrados no total.')
print(f'Foram {mulheres} mulheres cadastradas abaixo dos 20 anos.')
print('-'*25)
