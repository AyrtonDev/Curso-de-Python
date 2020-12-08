def metade(n=0, format=False):
    res = n / 2
    return res if format is False else moeda(n)


def dobro(n=0, format=False):
    res = n * 2
    return res if format is False else moeda(n)


def aumentar(n=0, por=0, format=False):
    '''
    -> Função quer serve para aumentar o preço em 15%
    :param n: Variavel que vem o preço
    :param por: Porcentagem para aumentar ou diminuir
    :param format: Para ativar a formatação de moeda
    '''
    p = n + (n * por / 100)
    return p if format is False else moeda(n)


def diminuir(n=0, por=0, format=False):
    p = n - (n * por / 100)
    return p if format is False else moeda(n)


def moeda(n=0, moeda = 'R$'):
    return f'{moeda}{n:.2f}'.replace('.',',')