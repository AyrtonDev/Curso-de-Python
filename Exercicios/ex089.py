alunos = list()
dados = list()

while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Nota 1: ')))
    dados.append(float(input('Nota 2: ')))
    alunos.append(dados[:])
    dados.clear()
    res = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if res == 'N':
        break
    else:
        print('-'*30)
print('-='*15)
print('No. Nome         MÉDIA')
print('-'*25)
for pos, a in enumerate(alunos):
    print(f'{pos}   {a[0]:<14}{(a[1] + a[2]) / 2:.1f}')
print('-'*25)
while True:
    esc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if esc == 999:
        break
    else:
        print(f'Notas de {alunos[esc][0]} são {alunos[esc][1:]}')
        print('-'*25)
print('-='*15)
print('FINALIZANDO...')
print('<<< VOLTE SEMPRE >>>')