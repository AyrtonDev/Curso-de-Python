# 1 versao do exercicio

'''print('Programa de PA')
print('Para sair, basta digita 0 termo!')
print('-'*20)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razao
while primeiro != 0:
    while primeiro < decimo:
        print('{} '.format(primeiro), end='-> ')
        primeiro += razao
    print('Acabou')
    print('-'*20)
    print('Digite Novamente!')
    primeiro = int(input('Primeiro termo: '))
    razao = int(input('Razão: '))
    decimo = primeiro + (10 - 1) * razao'''

# 2 versao do exercicio

print('Gerador de PA')
print('-='*10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))