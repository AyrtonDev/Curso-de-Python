# Aula sobre Tratamento de erros e Exceções
'''
primt(x)
'''
# Ao trocar N pelo M, temos um erro de sintaxe, e o outro problema é não ter declado x, gerando uma exceção d tipo NameError

# Exemplos de Exceção.:
'''
n = int(input('Número '))
print(f'Você digitou o número {n}')
'''
# se digitar oito numeral, o programa vai rodar normal, mas se digitarmos oito por extenso, vai ter uma exceção do tipo ValueError
'''
a = int(input('Numerador: '))
b = int(input('Denominador: '))
r = a / b
print(f'O resultado é {r}')
'''
# Neste caso, além da exceção ValueError, se o Denominador for 0, teremos a exceção do tipo ZeroDivisionError
'''
r = 2 / '2'
'''
# Neste havera a exceção do tipo TypeError
'''
lst = [3, 6, 4]
print(lst[3])
'''
# Este sera uma exceção do tipo IndexError
'''
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except Exception as erro:
    print(f'Problema encontrado foi {erro.__class__}')
else:
    print(f'O resultado é {r}')
finally:
    print('Volte sempre! Muito Obrigado!')
'''
# O comando try, irá testar o código
# except ira executar se o codigo digitado der erro, podemos passar parametros para capturar o tipo de erro, neste caso 'Exception as erro:'
# else é para quando estiver tudo perfeitamente
# finally sera executado indiferente se der certo ou errado o codigo. Obs.: else e finally sao opcionais.

try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (TypeError, ValueError):
    print('Tivemos um problema com os tipos de dados que você digitou.')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero!')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados!')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre! Muito Obrigado!')

# Um try pode ter varios except, e cada um pode ser programado para mostrar o tipo de erro.