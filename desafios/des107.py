# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções

from uteis import moeda

n = float(input('Digite um número qualquer: '))
print(f'O valor aumentado de 1 fica {moeda.aumentar(n)}')
print(f'O valor diminuido de 1 fica {moeda.diminuir(n)}')
print(f'O valor dobrado fica {moeda.dobro(n)}')
print(f'O valor pela metade fica {moeda.metade(n)}')