from datetime import date
print('Descubra se seu ano é BISSEXTO')
ano = int(input('Digite o seu ano: '))
if ano == 0:
    ano = date.today().year
res = ano % 4
if res == 0:
    print('O ano de {} é BISSEXTO.'.format(ano))
else:
    print('O ano de {} não é BISSEXTO'.format(ano))