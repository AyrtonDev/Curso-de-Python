def fatorial(n, show):
    f = 1
    print('-' * 30)
    for c in range(n, 0, -1):
        if show:
            print(f'{c}', end=' ')
            print('x' if c > 1 else '=', end=' ')
        f *= c
    print(f'{f}')


fatorial(5, show=True)