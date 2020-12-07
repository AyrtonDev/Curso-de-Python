from datetime import date

def voto(idade):
    res = ''    
    if idade < 16:
        res = 'NEGADO'
    elif idade == 16:
        res = 'OPCIONAL'
    elif idade < 65:
        res = 'OBRIGATÓRIO'
    else:
        res = 'OPCIONAL'
    return res


print('-' * 30)
nasc = int(input('Em que ano você nasceu? '))
if nasc == 0:
    print('Data de nascimento inválida')
else:
    ano = date.today().year
    idade = ano - nasc
    print(f'Com {idade} anos: voto {voto(idade)}!')

# Solução do professor

'''def voto(ano):
    from time import sleep
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: NÂO VOTA.'
    elif 16 <= idade < 18 or idade > 65:
        return f'com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'


nasc int(input('Em que ano você nasceu?'))
print(voto(nasc))'''