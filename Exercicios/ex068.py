from random import randint
print('='*25)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('='*25)
v = 0
while True:
    choice = ''
    num = 0
    cNum = randint(0, 10)
    while True:
        num = int(input('Diga um valor: '))
        if num < 0 or num > 10:
            print('+'*25)
            print('Número inválido! Digite um número entre 0 a 10!')
            print('+'*25)
        else:
            break
    while True:
        choice = str(input('Você quer par ou ímpar? ')).upper()
        if choice == 'IMPAR' or choice == 'PAR':
            break
        else:
            print('+'*25)
            print('Dado inválido! Digite novamente!')
            print('+'*25)
    result = (cNum + num) % 2
    if (num + cNum) == 0:
        print('Você e o computador jogaram 0! Tente de novo!')
        print('+'*25)
    else:
        print('~'*25)
        print(f'Você jogou {num} e o computador {cNum}. Total de {num + cNum} ', 'DEU PAR' if result == 0 else 'DEU IMPAR')
        print('~'*25)
        if choice == 'IMPAR':
            if result == 1:
                print('Você VENCEU!')
                print('Vamos jogar novamente...')
                print('='*25)
                v += 1
            else:
                print('Você PERDEU!')
                print('='*25)
                break
        elif choice == 'PAR':
            if result == 0:
                print('Você VENCEU!')
                print('Vamos jogar novamente...')
                print('='*25)
                v += 1
            else:
                print('Você PERDEU!')
                print('='*25)
                break
print(f'GAME OVER! Você venceu {v} vezes.')