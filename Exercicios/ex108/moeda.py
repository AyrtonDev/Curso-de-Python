def metade(n=0):
    return n / 2


def dobro(n=0):
    return n * 2


def aumentar(n=0, por=0):
    p = n + (n * por / 100)
    return p


def diminuir(n=0, por=0):
    p = n - (n * por / 100)
    return p

def moeda(n=0, moeda = 'R$'):
    return f'{moeda}{n:.2f}'.replace('.',',')