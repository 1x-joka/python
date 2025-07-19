# Adapte o código do desafio 107, criando uma função adicional chamada moeda() que consiga mostrar os valores como um valor monetário formatado

from uteis import moeda

n = float(input('Digite um número qualquer: '))
print(f'O valor aumentado de 1 fica {moeda.aumentar(n)}')
print(f'O valor diminuido de 1 fica {moeda.diminuir(n)}')
print(f'O valor dobrado fica {moeda.dobro(n)}')
print(f'O valor pela metade fica {moeda.metade(n)}')
print(f'O valor formatado pelo monetário fica {moeda.moeda(n)}')