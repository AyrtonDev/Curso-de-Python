from opções.menu import cor

def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print(f'{cor(1)}ERRO ao tentar abrir o arquivo!{cor(0)}')
    else:
        try:
            a.write(f'{nome}; {idade}\n')
        except:
            print(f'{cor(1)}ERRO ao escrever os dados!{cor(0)}')
        else:
            print(f'{cor(3)}Novo registro de {nome} adicionado.{cor(0)}')
            a.close()
    print('-' * 40)