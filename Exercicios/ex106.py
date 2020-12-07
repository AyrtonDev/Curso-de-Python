from time import sleep
c = (
    '\033[m',
    '\033[0;30;44m',
    '\033[0;30;42m',
    '\033[7;30m'
)

def paginaIni():
    print(c[2], end='')
    print('~' * 29)
    print('   SISTEMA DE AJUDA PyHELP   ')
    print('~' * 29)
    print(c[0], end='')
    sleep(1)


def log(met):
    print(c[1])
    print('~' * (35 + len(met)))
    print(f'  Acessando o manual do comando {met}  ')
    print('~' * (35 + len(met)))
    print(c[0])


def pesquisa(met):
    print(c[3])
    help(met)
    print(c[0])

while True:
    paginaIni()
    metodo = str(input('Função ou Biblioteca > ')).lower()
    if metodo == 'fim':
        break
    else:
        log(metodo)
        pesquisa(metodo)
print('~' * 13)
print('  ATÉ LOGO!')
print('~' * 13)

# Solução do professor

'''from time import sleep
c = (
    '\033[m',
    '\033[0;30;41m',
    '\033[0;30;42m',
    '\033[0;30;43m',
    '\033[0;30;44m',
    '\033[0;30;45m',
    '\033[7;30m'
)

def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(2)


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)


comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO!', 1)'''