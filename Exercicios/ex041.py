from datetime import date
cores = {
    'vermelho' : '\033[1;31m',
    'limpa' : '\033[m'
}

nasc = int(input('Ano de Nascimento: '))
print('--'*15)
atual = date.today().year
idade = atual - nasc
print('O atleta tem {} anos.'.format(idade))
print('--'*15)
if idade <= 9:
    print('Classificação: {}MIRIM{}'.format(cores['vermelho'], cores['limpa']))
elif idade <= 14:
    print('Classificação: {}INFANTIL{}'.format(cores['vermelho'], cores['limpa']))
elif idade <= 19:
    print('Classificação: {}JUNIOR{}'.format(cores['vermelho'], cores['limpa']))
elif idade <= 25:
    print('Classificação: {}SENIOR{}'.format(cores['vermelho'], cores['limpa']))
else:
    print('Classificação: {}MASTER{}'.format(cores['vermelho'], cores['limpa']))