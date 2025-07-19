# Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108

from uteis import moeda

n = float(input('Digite um número qualquer: '))
print(f'O valor aumentado de 1 fica {moeda.aumentar(n, True)}') # Para testar o programa, basta mudar True por False, ou vice-versa
print(f'O valor diminuido de 1 fica {moeda.diminuir(n, True)}')
print(f'O valor dobrado fica {moeda.dobro(n, True)}')
print(f'O valor pela metade fica {moeda.metade(n, True)}')