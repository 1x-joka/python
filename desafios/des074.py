# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla

import random
tupla = (
    random.randint(0,5),
    random.randint(0,5),
    random.randint(0,5),
    random.randint(0,5),
    random.randint(0,5)
)

print(f'Os valores escolhidos foram: {tupla}')
print(f'O maior valor sorteado foi: {max(tupla)}')
print(f'O menor valor sorteado foi: {min(tupla)}')