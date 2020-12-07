def escreva(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)


for c in range(0, 3): 
    escreva(str(input('Digite um algo: ')))


# Solução do Professor
'''def escreva(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)


escreva('Gustavo Guanabara')
escreva('Curso de Python no YouTube')
escreva('CeV')'''