cores = {
    'fundoAmarelo' : '\033[43;32m',
    'lilas' : '\033[35m',
    'azul' : '\033[34m',
    'vermelho' : '\033[31m',
    'limpa' : '\033[m'
}

print(cores['fundoAmarelo'], '-='*15, cores['limpa'])
print(cores['fundoAmarelo'], 'Conversor de Base Numerica', cores['limpa'])
print(cores['fundoAmarelo'], '-='*15, cores['limpa'])

num = int(input('Digite um numero inteiro: '))
print(cores['fundoAmarelo'], '-='*15, cores['limpa'])
print('Selecione o tipo de conversao:')
print('1 - BINARIO')
print('2 - OCTAL')
print('3 - HEXADECIMAL')
escolha = int(input('Sua opção: '))
print(cores['fundoAmarelo'], '-='*15, cores['limpa'])

if escolha == 1:
    print('{}O numero {} em BINARIO fica {}.{}'.format(cores['lilas'], num, bin(num)[2:], cores['limpa']))
elif escolha == 2:
    print('{}O numero {} em OCTAL fica {}.{}'.format(cores['azul'], num, oct(num)[2:], cores['limpa']))
elif escolha == 3:
    print('{}O numero {} em HEXADECIMAL fica {}.{}'.format(cores['vermelho'], num, hex(num)[2:], cores['limpa']))
else:
    print('Opção inválida. Tente Novamente.')
