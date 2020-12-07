pessoa = dict()
cadastro = list()
tot = 0
while True:
    sexo = ''
    res = ''
    pessoa['nome'] = str(input('Nome: '))
    while True:
        sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
        if sexo in 'MF':
            break
        else:
            print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['sexo'] = sexo
    pessoa['idade'] = int(input('Idade: '))
    tot += pessoa["idade"]
    cadastro.append(pessoa.copy())
    pessoa.clear()
    while True:
        res = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if res in 'NS':
            break
        else:
            print('ERRO! Responda apenas S ou N.')
    if res == 'N':
        break
    print('--'*25)
print('-='*25)
print(f'- O grupo tem {len(cadastro)} pessoas.')
print(f'- A média de idade é {tot / len(cadastro):.2f} anos.')
print(f'- As mulheres cadastradas foram: ', end='')
for c in cadastro:
    if c["sexo"] == 'F':
        print(f'{c["nome"]}', end=' ')
print()
print('- Lista das pessoas que estão acima da média:')
for c in cadastro:
    if c["idade"] > (tot / len(cadastro)):
        for k, v in c.items():
            print(f'{k} = {v};', end=' ')
        print()
print('<< ENCERRADO >>')