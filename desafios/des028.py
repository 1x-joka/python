# Escreva um programa que faça o computador pensar em um número inteiro entre 0 e 5 e peça para o usuário descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu

import random
computador = random.randint(0,5) # Faz o computador "Pensar" (Escolhe qualquer um)

numero = int(input('Digite o número que você acha que eu pensei: '))

if numero == computador:
    print('VOCÊ GANHOU!!')
else:
    print('VOCÊ PERDEU!! Eu pensei no número {}'.format(computador))