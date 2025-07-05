# Faça um programa que faça o computador jogar Jokenpô com você

import random
lista = ['Pedra', 'Papel', 'Tesoura']

print('''Escolha...
[ 1 ] - Pedra
[ 2 ] - Papel
[ 3 ] - Tesoura''')
jogador = int(input('Escolha uma opção: '))
computador = random.randint(1,3)

jogada_jogador = lista[jogador - 1] # converte o número 1/2/3 para "Pedra", "Papel" ou "Tesoura"
jogada_computador = lista[computador - 1] # -1 pois,em uma lista, o primeiro elemento tem índice 0, então se o computador escolher 1, na verdade é o elemento 0

if jogador == computador:
    print('EMPATAMOS! Eu escolhi {} e você {}'.format(jogada_computador, jogada_jogador))
elif jogador == 1 and computador == 2:
    print('GANHEI! Eu escolhi {} e você {}'.format(jogada_computador, jogada_jogador))
elif jogador == 1 and computador == 3:
    print('PERDI! Eu escolhi {} e você {}'.format(jogada_computador, jogada_jogador))
elif jogador == 2 and computador == 1:
    print('PERDI! Eu escolhi {} e você {}'.format(jogada_computador, jogada_jogador))
elif jogador == 2 and computador == 3:
    print('GANHEI! Eu escolhi {} e você {}'.format(jogada_computador, jogada_jogador))
elif jogador == 3 and computador == 1:
    print('GANHEI! Eu escolhi {} e você {}'.format(jogada_computador, jogada_jogador))
elif jogador == 3 and computador == 2:
    print('PERDI! Eu escolhi {} e você {}'.format(jogada_computador, jogada_jogador))
else:
    print('[ERRO] DIGITE VALORES VÁLIDOS')