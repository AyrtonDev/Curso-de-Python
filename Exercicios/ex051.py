first = int(input('Primeiro termo: '))
reason = int(input('Razão: '))
tenth = first + (10 - 1) * reason
for c in range(first, tenth, reason):
    print('{} '.format(c), end=' -> ')
print('ACABOU')