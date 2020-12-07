cores = {
    'limpa' : '\033[m',
    'vermelho' : '\033[1;31m',
    'azul' : '\033[1;34m'
}

print('=-'*15)
print('|      Analisador de Nota     |')
print('=-'*15)

nome = str(input('Nome do aluno: '))
print('-'*20)
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
nota3 = float(input('Terceira nora: '))
print('-'*20)

media = (nota1 + nota2 + nota3) / 3

print('O aluno teve media {:.1f}.'.format( media))
if media < 5:
    print('O aluno {} esta {}REPROVADO{}.'.format(nome, cores['vermelho'], cores['limpa']))
elif media < 6.9:
    print('O aluno {} esta em {}RECUPERAÇAO{}.'.format(nome, cores['vermelho'], cores['limpa']))
else:
    print('O aluno {} esta {}APROVADO{}.'.format(nome, cores['azul'], cores['limpa']))