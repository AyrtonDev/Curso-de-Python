from datetime import date
ano = date.today().year
trabalhador = dict()
trabalhador['nome'] = str(input('Nome: '))
trabalhador['idade'] = ano - int(input('Ano de Nascimento: '))
trabalhador['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if trabalhador["ctps"] == 0:
    print('-='*25)
    print(f'- Nome tem o valor {trabalhador["nome"]}')
    print(f'- idade tem o valor {trabalhador["idade"]}')
    print(f'- Ctps tem o valor {trabalhador["ctps"]}')
else:
    trabalhador['contratação'] = int(input('Ano de Contratação: '))
    trabalhador['salario'] = int(input('Salário: R$ '))
    print('-='*25)
    print(f'- Nome tem o valor {trabalhador["nome"]}')
    print(f'- idade tem o valor {trabalhador["idade"]}')
    print(f'- Ctps tem o valor {trabalhador["ctps"]}')
    print(f'- contratação tem valor {trabalhador["contratação"]}')
    print(f'- salário tem o valor {trabalhador["salario"]:.1f}')
    trabalhador['aposentadoria'] = (trabalhador["contratação"] + 35) - (ano - trabalhador["idade"])
    print(f'- aposentadoria tem o valor {trabalhador["aposentadoria"]}')

# Solução do Professor
'''from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de Contratação: '))
    dados['salario'] = float(input('Salário: R$'))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
print('-='*30)
for k, v in dados.items():
    print(f'  - {k} tem o valor {v}')'''