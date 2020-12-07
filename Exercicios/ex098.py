from time import sleep

def contador(i, f, p):
    uno = 0
    if f > i:
        uno = 1 
    else:
        uno = -1
    if p == 0:
        p = 1
    if i > f and p > 0:
        p = -p
    elif i < f and p < 0:
        p = abs(p)
    print('-=' * 30)
    print(f'Contagem de {i} até {f} de {abs(p)} em {abs(p)}')
    for c in range(i, f+uno, p):
        sleep(0.5)
        print(f'{c}', end=' ')
    print('FIM!')


contador(1, 10, 1)
contador(10, -1, 2)
print('-=' * 30)
print('Agora é sua vez de personalizar a contagem!')
init = int(input('Início: '))
fim = int(input('Fim '))
passo = int(input('Passo: '))
contador(init, fim, passo)

# Solução do Professor

'''def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('-=' * 20)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(2.5)

    if i <f:
        cont = i
        while cont <= f:
            print(f'{cont} ',end='', flush=True)
            sleep(0.5)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ',end='', flush=True)
            sleep(0.5)
            cont -= p
        print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 20)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim:    '))
pas = int(input('Passo:  '))
contador(ini, fim, pas)'''