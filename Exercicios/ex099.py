from time import sleep

def maior(lst):
    maior = 0
    print('-=' * 30)
    print('Analisando os valores passados...')
    if len(lst) == 0:
        print('Foram informados 0 valores ao todo.')
        print('O maior valor informado foi 0.')
    else:
        for c in lst:
            print(f'{c}', end=' ')
            sleep(0.5)
            if maior < c:
                maior = c
        print(f'Foram informados {len(lst)} valores ao todo.')
        sleep(0.5)
        print(f'O maior valor informado foi {maior}.')

maior([2, 9, 4, 5, 7, 1])
maior([4, 7, 0])
maior([1, 2])
maior([6])
maior([])

# Solução do Professor

'''def maior(* num):
    cont = maior = 0
    print('-=' * 30)
    print('Analisando os valores passados... ')
    for valor in num:
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maor valor informado foi {maior}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()'''