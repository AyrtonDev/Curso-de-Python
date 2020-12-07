from datetime import date
cores = {
    'limpa' : '\033[m',
    'lilas' : '\033[4;35m',
    'vermelho' : '\033[1;31m'
}

nasc = int(input('Ano de nascimento: '))
data = date.today().year
idade = data - nasc
print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, data))
if idade < 18:
    print('Ainda falta {}{} anos{} para o alistamento'.format(cores['lilas'], (18 - idade), cores['limpa']))
    print('Seu alistamento sera em {}{}{}.'.format(cores['vermelho'], (nasc + 18), cores['limpa']))
elif idade == 18:
    print('Voce tem que se alistar {}IMEDIATAMENTE{}!'.format(cores['vermelho'], cores['limpa']))
else:
    print('Voce ja deveria ter se alistado ha {}{} anos{}.'.format(cores['vermelho'], (idade - 18), cores['limpa']))
    print('Seu alistamento foi em {}{}{}.'.format(cores['lilas'], (nasc + 18), cores['limpa']))