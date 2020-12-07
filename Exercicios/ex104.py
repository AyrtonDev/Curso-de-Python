cores = {
    'limpa' : '\033[m',
    'vermelho' : '\033[31m',
    'azulBold' : '\033[1;34m'
}

def leiaInt(n):
    while True:
        num = input(n)
        if num.isnumeric():
            break
        else:
            print(f'{cores["vermelho"]}ERRO! Digite um número inteiro válido{cores["limpa"]}')
    return num


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {cores["azulBold"]}{n}{cores["limpa"]}')