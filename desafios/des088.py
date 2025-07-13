# Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta

from random import randint
from time import sleep
lista = list()
jogos = list()
print('-'*30)
print('     Programa MEGA SENA      ')
print('-'*30)
qtd = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1

while tot <= qtd: # Enquanto o total de jogadas chegar nas digitadas...
    cont = 0
    while True:
        numero = randint(1, 60)
        if numero not in lista: # Se o número sorteado NÃO estiver na lista...
            lista.append(numero)
            cont += 1
        if cont >= 6: # Se ja foram sorteados 6 números...
            break
    lista.sort()
    jogos.append(lista[:]) # Criando uma lista grande (jogos) cheia de listas pequenas (lista)
    lista.clear()
    tot += 1 # Para não entrar em loop infinito
print('-='*3, f'Sorteando {qtd} jogos', '-='*3)

for indice, l in enumerate(jogos): # Para cada índice e lista...
    print(f'Jogo {indice + 1}: {l}') # Mostra esse painelzinho
    sleep(1) # Esperando 1 segundo a cada print
print('-='*5, '< BOA SORTE! >', '-='*5)