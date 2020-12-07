from time import sleep
cores = {
    'limpa' : '\033[m',
    'ciano' : '\033[36m',
    'verde' : '\033[32m',
    'vermelhoUnder' : '\033[31;4m'
}
print(cores['verde'],'-='*15,cores['limpa'])
print('  {}Sistema de Emprestimo{}'.format(cores['vermelhoUnder'], cores['limpa']))
print(cores['verde'],'-='*15,cores['limpa'])

valorCasa = float(input('Qual o valor da casa para o emprestimo? '))
salario = float(input('Qual o valor do seu salario? '))
pagAno = int(input('Em quantos anos voce ira pagar o emprestimo? '))

pagMensal = pagAno * 12
parcelamento = valorCasa / pagMensal
print('{}PROCESSANDO...{}'.format(cores['ciano'], cores['limpa']))
sleep(2)
if (salario * 30 / 100) <= parcelamento:
    print('Emprestimo {}NEGADO{}'.format(cores['vermelhoUnder'], cores['limpa']))
else:
    print('Emprestimo {}APROVADO{}'.format(cores['ciano'], cores['limpa']))
    print('O parcelamento ficara de {}x de {:.2f} reais'.format(pagMensal, parcelamento))