def nota(* notas, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    dados = dict()
    dados['total'] = len(notas)
    dados['maior'] = max(notas)
    dados['menor'] = min(notas)
    dados['média'] = sum(notas) / len(notas)
    if sit:
        if dados['média'] < 6:
            dados['situação'] = 'RUIM'
        elif dados['média'] < 7:
            dados['situação'] = 'RAZOAVEL'
        else:
            dados['situação'] = 'BOA'
    return dados


resp = nota(5.5, 2.5, 1.5, sit=True)
print('-' * 30)
print(resp)