# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações: Quantidade de notas, a maior nota, a menor nota, a média da turma e a situação(opcional). Adicione também as docstrings da função

def notas(*num, situacao = False):
    """
    --> Função para analisar notas e situações de alunos
    :param num: uma ou mais notas dos alunos (aceita várias)
    :type num: float
    :param situacao: valor opcional indicando se deve ou não adicionar a situação
    :type situacao: booleano
    :return: dicionário com várias informações sobre a situação da turma
    :rtype: dict
    """
    r = {}
    r['total'] = len(num)
    r['maior'] = max(num)
    r['menor'] = min(num)
    r['media'] = sum(num) / len(num)
    if situacao == True:
        if r['media'] >= 7:
            r['situacao'] = 'BOA'
        elif r['media'] >= 5:
            r['situacao'] = 'RAZOÁVEL'
        else:
            r['situacao'] = 'RUIM'
    return r

# Programa Principal
resp = notas(9, 10, 5.5, 2.5, 8.5, situacao=True)
print(resp)
# help(notas)