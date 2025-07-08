# Faça um programa que jogue par ou ímpar. O jogo só sera interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo

print('='*20, 'Programa Par ou Ímpar', '='*20)
import random
ganhou = 0
total = 0

while True:
    computador = random.randint(0, 10) # Tem que colocar dentro do while para o número não ser o mesmo
    pergunta = input('Par ou Ímpar: ').strip().upper()[0]
    jogador = int(input('Digite o número: '))
    total = computador + jogador
    if pergunta == 'P' and total % 2 != 0 or pergunta == 'I' and total % 2 == 0:
        print(f'PERDEU! Eu escolhi {computador}')
        break
    else:
        print('GANHOU! Denovo..')
        ganhou += 1
print(f'Você ganhou {ganhou} rodadas consecutivas!')