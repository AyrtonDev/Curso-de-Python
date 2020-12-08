def leiaDinheiro(p):
    while True:
        preço = str(input(f'{p}').replace(',','.').strip())
        if preço.isalpha() or preço == '':
            print(f'\033[0;31mERRO: "{preço}" é um preço inválido!\033[m')
        else:
            break
    return float(preço)