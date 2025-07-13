# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado

from random import randint
from time import sleep
from operator import itemgetter

resultados = {
    'Jogador 1': randint(1, 6),
    'Jogador 2': randint(1, 6),
    'Jogador 3': randint(1, 6),
    'Jogador 4': randint(1, 6)
}
ranking = dict()
print('\nValores Sorteados:')

for jogador, valor in resultados.items():
    print(f'O {jogador} tirou {valor}')
    sleep(1)

ranking = sorted(resultados.items(), key=itemgetter(1), reverse=True) # Se a posição for 0 ele vai colocar em ordem de chave, se for posição 1 ele vai colocar em ordem de valor / Colocando do maior para o menor

print('-='*20)
print('==   RANKING DOS JOGADORES     ==')
for i, v in enumerate(ranking):
    print(f'{i + 1}° lugar: {v[0]} com {v[1]}') # v[0] = Nome do Jogador e v[1] = Valor sorteado
    sleep(1)