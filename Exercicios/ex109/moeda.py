def metade(n=0, format=False):
    res = n / 2
    return res if format is False else moeda(n)


def dobro(n=0, format=False):
    res = n * 2
    return res if format is False else moeda(n)


def aumentar(n=0, por=0, format=False):
    p = n + (n * por / 100)
    return p if format is False else moeda(n)


def diminuir(n=0, por=0, format=False):
    p = n - (n * por / 100)
    return p if format is False else moeda(n)

def moeda(n=0, moeda = 'R$'):
    return f'{moeda}{n:.2f}'.replace('.',',')