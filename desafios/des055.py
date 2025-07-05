# Faça um programa que leia o peso de cinco pessoas. No final mostre qual foi o maior e o menor peso lidos

maior = 0
menor = 0

for c in range(1, 6):
    peso = float(input(f'Digite o peso (em kg) da {c}° pessoa: '))
    if c == 1: # Primeiro peso inserido
        maior = peso
        menor = peso
    elif peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
print(f'O menor peso foi {menor}kg')
print(f'O maior peso foi {maior}kg')