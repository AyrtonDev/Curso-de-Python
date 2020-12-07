# Aula ensina modificações com cores pelo padrão ANSI

print('\033[0;30;41mTeste!\033[m')
print('\033[4;33;44mTeste!\033[m')
print('\033[1;35;43mTeste\033[m')
print('\033[0;30;42mTeste!\033[m')
print('\033[30;42mTeste!\033[m')
print('\033[mTeste')
print('\033[7;30mTeste!\033[m')

nome = 'Ayrton'

print('Olá! Muito prazer em te conhecer, {}{}{}!!'.format('\033[4;34m', nome, '\033[m'))

cores = {
    'limpa' : '\033[m',
    'azul' : '\033[34m',
    'amarelo' : '\033[33m',
    'pretobranco' : '\033[7;30m'
}

print('Olá! Muito prazer em te conhecer, {}{}{}!!'.format(cores['amarelo'], nome, cores['limpa']))
