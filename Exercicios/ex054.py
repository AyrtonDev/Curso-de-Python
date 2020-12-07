from datetime import date
data = date.today().year
maiorIdade = 0
menorIdade = 0
for c in range(1, 8):
    pessoa = int(input('Em que ano a {}ª pessoa nasceu? '.format(c)))
    if (data - pessoa) >= 21:
        maiorIdade += 1
    else:
        menorIdade += 1

print('')
if maiorIdade == 0:
    print('Não tivemos pessoas maiores de idade')
elif maiorIdade == 1:
    print('Ao todo tivemos {} pessoa maior de idade'.format(maiorIdade))
else:
    print('Ao todo tivemos {} pessoas maiores de idade'.format(maiorIdade))

if menorIdade == 0:
    print('Não tivemos pessoas menores de idade')
elif menorIdade == 1:
    print('Ao todo tivemos {} pessoa menor de idade'.format(menorIdade))
else:
    print('Ao todo tivemos {} pessoas menores de idade'.format(menorIdade))