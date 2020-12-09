cores = {
    'limpa' : '\033[m',
    'vermelho' : '\033[31m',
    'azulBold' : '\033[1;34m'
}

def leiaInt(n):
    while True:
        try:
            num = int(input(n))
        except (ValueError, TypeError):
            print(f'{cores["vermelho"]}ERRO: por favor, digite um número inteiro válido.{cores["limpa"]}')
            continue
        except KeyboardInterrupt:
            print(f'{cores["vermelho"]}Usuário preferiu nãi digitar esse número.{cores["limpa"]}')
            return 0
        else:
            return num


def leiaFloat(n):
    while True:
        try:
            num = float(input(n))
        except (ValueError, TypeError):
            print(f'{cores["vermelho"]}ERRO: por favor, digite um número real válido.{cores["limpa"]}')
            continue
        except KeyboardInterrupt:
            print(f'{cores["vermelho"]}Usuário preferiu nãi digitar esse número.{cores["limpa"]}')
            return 0
        else:
            return num


i = leiaInt('Digite um Inteiro: ')
r = leiaFloat('Digite um Real: ')
print(f'O valor inteiro digitado foi {cores["azulBold"]}{i}{cores["limpa"]} e o real foi {cores["azulBold"]}{r}{cores["limpa"]}')