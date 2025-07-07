# Melhore o jogo do desafio 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer

import random
computador = random.randint(0, 10)
jogador = int(input('Digite o número que o computador pensou: '))

palpite = 1

while jogador != computador:
    jogador = int(input('Errou, tente novamente: '))
    palpite += 1
print(f'Acertou! Ao todo tiveram {palpite} tentativas!')